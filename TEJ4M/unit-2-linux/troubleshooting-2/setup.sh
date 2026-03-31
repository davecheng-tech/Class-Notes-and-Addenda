#!/bin/bash
# =============================================================
# TEJ4M — Troubleshooting Exercise 2 Setup Script
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
echo " TEJ4M Troubleshooting Exercise 2 — Setup"
echo " Student user: $STUDENT_USER"
echo " Home directory: $STUDENT_HOME"
echo "=================================================="
echo ""


# ----------------------------------------------------------
# SCENARIO 4 — Execute bit + log file permissions
# ----------------------------------------------------------
echo "[1/3] Setting up Scenario 4 (execute + file permissions)..."

# Create the stats log — root-owned, chmod 600 so student cannot read it
touch /var/log/retrogames-stats.log
chown root:root /var/log/retrogames-stats.log
chmod 600 /var/log/retrogames-stats.log

# Pre-populate log with session data
cat >> /var/log/retrogames-stats.log << 'LOGEOF'
2026-03-30 14:01:05 [SESSION] player=kanzaki game=galaga score=12400 duration=8m
2026-03-30 14:09:22 [SESSION] player=morrow game=pacman score=8800 duration=5m
2026-03-30 14:15:03 [SESSION] player=kanzaki game=centipede score=21600 duration=12m
2026-03-30 14:27:44 [SESSION] player=wu game=galaga score=9100 duration=6m
2026-03-30 14:33:59 [SESSION] player=morrow game=centipede score=15200 duration=9m
LOGEOF

# Create the stats script — chmod 644 (no execute bit)
# The script explicitly checks readability so error messages are deterministic.
cat > /usr/local/bin/rg-stats << 'EOF'
#!/bin/bash
LOG=/var/log/retrogames-stats.log

if [ ! -r "$LOG" ]; then
    echo "ERROR: Cannot read stats log at $LOG"
    echo "       Check file permissions."
    exit 1
fi

echo "=== RetroGames Session Statistics ==="
echo ""
echo "Recent sessions:"
grep "\[SESSION\]" "$LOG" | tail -5 | while IFS= read -r line; do
    echo "  $line"
done
echo ""
COUNT=$(grep -c "\[SESSION\]" "$LOG")
echo "Total sessions logged: $COUNT"
EOF

chown root:root /usr/local/bin/rg-stats
chmod 644 /usr/local/bin/rg-stats    # no execute bit — first obstacle

echo "    Done."


# ----------------------------------------------------------
# SCENARIO 5 — Config file: ownership + bad value + missing dir
# ----------------------------------------------------------
echo "[2/3] Setting up Scenario 5 (highscore server config)..."

mkdir -p /etc/retrogames

# Write config with one bad value (max_entries is not a number)
# and one missing directory (data_dir)
cat > /etc/retrogames/highscores.conf << 'CONFEOF'
# RetroGames Highscore Server Configuration
max_entries=one-hundred
data_dir=/opt/retrogames/scores
leaderboard_name=RetroGames Hall of Fame
CONFEOF

# Problem 1: wrong ownership — root owns it
# Problem 2: permissions 600 — student user cannot read it
chown root:root /etc/retrogames/highscores.conf
chmod 600 /etc/retrogames/highscores.conf

# Problem 3: max_entries=one-hundred (not a number — must be e.g. 100)
# Problem 4: data_dir /opt/retrogames/scores does not exist
# (Do NOT create /opt/retrogames/scores — that would fix it)
# Note: /opt/retrogames itself may or may not exist from exercise 1.
# Either way, the scores subdirectory must not exist.
rm -rf /opt/retrogames/scores 2>/dev/null || true

echo "    Done."


# ----------------------------------------------------------
# SCENARIO 6 — Script execute bit + config at wrong path + missing dir
# ----------------------------------------------------------
echo "[3/3] Setting up Scenario 6 (media server)..."

mkdir -p /etc/retrogames

# Config placed at wrong filename (.bak) — student must copy/rename it
cat > /etc/retrogames/media.conf.bak << 'CONFEOF'
# RetroGames Media Server Configuration
stream_dir=/var/lib/retrogames/streams
max_connections=10
CONFEOF

chown root:root /etc/retrogames/media.conf.bak
chmod 644 /etc/retrogames/media.conf.bak   # readable once found, just wrong name

# Ensure there is no media.conf at the correct path
rm -f /etc/retrogames/media.conf

# Create the media server script — chmod 644 (no execute bit)
# Script explicitly reports each failure condition so errors are deterministic.
cat > /usr/local/bin/rg-media << 'EOF'
#!/bin/bash
CONF=/etc/retrogames/media.conf

if [ ! -f "$CONF" ]; then
    echo "ERROR: Configuration file not found at $CONF"
    echo "       Check whether the file exists in /etc/retrogames/"
    exit 1
fi

if [ ! -r "$CONF" ]; then
    echo "ERROR: Cannot read configuration file at $CONF"
    echo "       Check file permissions."
    exit 1
fi

STREAM_DIR=$(grep "^stream_dir=" "$CONF" | cut -d= -f2)
MAX_CONN=$(grep "^max_connections=" "$CONF" | cut -d= -f2)

if [ -z "$STREAM_DIR" ]; then
    echo "ERROR: stream_dir not set in $CONF"
    exit 1
fi

if [ ! -d "$STREAM_DIR" ]; then
    echo "ERROR: Stream directory does not exist: $STREAM_DIR"
    echo "       Create it before starting the media server."
    exit 1
fi

echo "RetroGames Media Server"
echo "Stream directory: $STREAM_DIR"
echo "Max connections:  $MAX_CONN"
echo "Status: ready"
EOF

chown root:root /usr/local/bin/rg-media
chmod 644 /usr/local/bin/rg-media    # no execute bit — first obstacle

# Ensure the stream directory does not exist
rm -rf /var/lib/retrogames 2>/dev/null || true

echo "    Done."


echo ""
echo "=================================================="
echo " Setup complete."
echo ""
echo " Distribute to students:"
echo "   scenario-4/README.md"
echo "   scenario-5/README.md + verify.sh"
echo "   scenario-6/README.md + verify.sh"
echo "=================================================="
