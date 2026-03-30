#!/bin/bash
# =============================================================
# TEJ4M — Troubleshooting Exercise Teardown Script
# Run with: sudo bash teardown.sh
# =============================================================

if [ "$EUID" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    exit 1
fi

echo "Tearing down troubleshooting exercise..."

# Kill scenario 2 processes (ignore errors if already dead)
pkill -9 -f "retrogames/monitord.sh" 2>/dev/null || true
pkill -9 -f "retrogames/worker.sh"   2>/dev/null || true

# Remove all created files and directories
rm -f  /usr/local/bin/launcher
rm -rf /opt/retrogames
rm -rf /usr/local/lib/retrogames
rm -f  /var/log/retro-monitor.log
rm -rf /etc/retrogames

echo "Done. All scenarios removed."
