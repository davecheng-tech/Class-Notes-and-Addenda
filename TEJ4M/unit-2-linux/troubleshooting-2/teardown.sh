#!/bin/bash
# =============================================================
# TEJ4M — Troubleshooting Exercise 2 Teardown Script
# Run with: sudo bash teardown.sh
#
# Removes only files created by setup.sh for this exercise.
# Safe to run independently of the original troubleshooting/teardown.sh.
# =============================================================

if [ "$EUID" -ne 0 ]; then
    echo "ERROR: This script must be run with sudo."
    exit 1
fi

echo "Tearing down troubleshooting exercise 2..."

# Scenario 4
rm -f  /usr/local/bin/rg-stats
rm -f  /var/log/retrogames-stats.log

# Scenario 5
rm -f  /etc/retrogames/highscores.conf
rm -rf /opt/retrogames/scores

# Scenario 6
rm -f  /usr/local/bin/rg-media
rm -f  /etc/retrogames/media.conf
rm -f  /etc/retrogames/media.conf.bak
rm -rf /var/lib/retrogames

# Remove /etc/retrogames only if empty (may be shared with exercise 1)
rmdir /etc/retrogames 2>/dev/null || true

echo "Done. All exercise 2 scenarios removed."
