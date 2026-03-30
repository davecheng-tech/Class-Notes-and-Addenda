#!/bin/bash
# =============================================================
# TEJ4M — Troubleshooting Exercise Setup Script
# Run with: sudo bash setup.sh
# =============================================================

set -e

# Verify running as root
if [ "$EUID" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    echo "Usage: sudo bash setup.sh"
    exit 1
fi

# Determine the actual student user (not root)
STUDENT_USER="${SUDO_USER:-$(logname 2>/dev/null)}"
if [ -z "$STUDENT_USER" ] || [ "$STUDENT_USER" = "root" ]; then
    echo "ERROR: Could not determine the student user account."
    echo "Run as: sudo bash setup.sh (not as root directly)"
    exit 1
fi

STUDENT_HOME=$(getent passwd "$STUDENT_USER" | cut -d: -f6)

echo "=================================================="
echo " TEJ4M Troubleshooting Exercise — Setup"
echo " Student user: $STUDENT_USER"
echo " Home directory: $STUDENT_HOME"
echo "=================================================="
echo ""


# ----------------------------------------------------------
# SCENARIO 1 — Wrong architecture + permissions + PATH
# ----------------------------------------------------------
echo "[1/3] Setting up Scenario 1 (architecture mismatch)..."

# Create a fake ARM64 ELF binary — correct magic bytes so `file` identifies it as aarch64
# ELF header bytes: magic, 64-bit, little-endian, version 1, OSABI 0, padding, ET_EXEC, EM_AARCH64
TMP_ARM=$(mktemp)
printf '\x7f\x45\x4c\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00' > "$TMP_ARM"
dd if=/dev/zero bs=1 count=100 >> "$TMP_ARM" 2>/dev/null
cp "$TMP_ARM" /usr/local/bin/launcher
rm "$TMP_ARM"
chmod 644 /usr/local/bin/launcher        # no execute bit — first obstacle

# Create the real x86_64 launcher (a shell script) in a non-PATH location
mkdir -p /opt/retrogames
cat > /opt/retrogames/launcher << 'EOF'
#!/bin/bash
echo "RetroGames Launcher v1.0"
echo "Architecture: $(uname -m)"
echo "System ready. Load a ROM to begin."
EOF
chmod 644 /opt/retrogames/launcher       # no execute bit — must be fixed
chown root:root /opt/retrogames/launcher

echo "    Done."


# ----------------------------------------------------------
# SCENARIO 2 — Runaway daemon with respawning workers
# ----------------------------------------------------------
echo "[2/3] Setting up Scenario 2 (runaway process)..."

mkdir -p /usr/local/lib/retrogames

# Worker script — runs in a loop writing to a log
cat > /usr/local/lib/retrogames/worker.sh << 'EOF'
#!/bin/bash
LOG=/var/log/retro-monitor.log
while true; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') [WORKER $$] scanning rom library..." >> "$LOG"
    sleep 3
done
EOF
chmod +x /usr/local/lib/retrogames/worker.sh

# Monitor daemon — ignores SIGTERM, respawns worker if it dies
cat > /usr/local/lib/retrogames/monitord.sh << 'EOF'
#!/bin/bash
trap '' SIGTERM    # ignore polite kill — must use SIGKILL
LOG=/var/log/retro-monitor.log
WORKER_PID=""

spawn_worker() {
    bash /usr/local/lib/retrogames/worker.sh &
    WORKER_PID=$!
    echo "$(date '+%Y-%m-%d %H:%M:%S') [MONITOR] worker spawned (pid $WORKER_PID)" >> "$LOG"
}

echo "$(date '+%Y-%m-%d %H:%M:%S') [MONITOR] retro-monitord started (pid $$)" >> "$LOG"
spawn_worker

while true; do
    if ! kill -0 "$WORKER_PID" 2>/dev/null; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') [MONITOR] worker died — respawning..." >> "$LOG"
        spawn_worker
    fi
    sleep 2
done
EOF
chmod +x /usr/local/lib/retrogames/monitord.sh

# Create log file owned by student user (daemon runs as student)
touch /var/log/retro-monitor.log
chown "$STUDENT_USER":"$STUDENT_USER" /var/log/retro-monitor.log
chmod 644 /var/log/retro-monitor.log

# Pre-populate log with history so there's something to grep
cat >> /var/log/retro-monitor.log << 'LOGEOF'
2026-03-25 09:12:01 [MONITOR] retro-monitord started (pid 1823)
2026-03-25 09:12:01 [MONITOR] worker spawned (pid 1824)
2026-03-25 09:12:01 [WORKER 1824] scanning rom library...
2026-03-25 09:12:04 [WORKER 1824] scanning rom library...
2026-03-25 09:12:07 [ERROR] rom directory not found — retrying indefinitely
2026-03-25 09:12:07 [WORKER 1824] scanning rom library...
2026-03-25 09:12:10 [ERROR] rom directory not found — retrying indefinitely
LOGEOF

# Launch daemon as student user
sudo -u "$STUDENT_USER" bash -c \
    'nohup bash /usr/local/lib/retrogames/monitord.sh >/dev/null 2>&1 &'

echo "    Done."


# ----------------------------------------------------------
# SCENARIO 3 — Broken config file (3 problems)
# ----------------------------------------------------------
echo "[3/3] Setting up Scenario 3 (broken config)..."

mkdir -p /etc/retrogames

# Write config with two bad values:
#   - log_level=DEBG (typo — not a valid level)
#   - rom_path points to a directory that doesn't exist
cat > /etc/retrogames/retrogames.conf << CONFEOF
# RetroGames Configuration
data_dir=/opt/retrogames/data
log_level=DEBG
max_players=4
rom_path=${STUDENT_HOME}/roms
CONFEOF

# Problem 1: wrong ownership — root owns it
# Problem 2: permissions 600 — student user cannot read it
chown root:root /etc/retrogames/retrogames.conf
chmod 600 /etc/retrogames/retrogames.conf

# (Problem 3 is the bad log_level value; Problem 4 is the missing rom_path directory)
# verify.sh checks all three: readability, log_level validity, rom_path existence

echo "    Done."


echo ""
echo "=================================================="
echo " Setup complete."
echo ""
echo " Distribute to students:"
echo "   scenario-1/README.md"
echo "   scenario-2/README.md"
echo "   scenario-3/README.md + verify.sh"
echo "=================================================="
