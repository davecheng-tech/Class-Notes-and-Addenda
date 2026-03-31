#!/bin/bash
# =============================================================
# Scenario 5 — Highscore Server Configuration Verifier
# Run with: bash verify.sh
# =============================================================

CONF=/etc/retrogames/highscores.conf
PASS=0
FAIL=0

check() {
    local label="$1"
    local result="$2"
    local hint="$3"
    if [ "$result" = "pass" ]; then
        echo "  [PASS] $label"
        ((PASS++))
    else
        echo "  [FAIL] $label${hint:+  →  $hint}"
        ((FAIL++))
    fi
}

echo ""
echo "=== RetroGames Highscore Server — Configuration Check ==="
echo ""

# Check 1: Is the config file readable?
if [ -r "$CONF" ]; then
    check "Config file is readable by current user" pass
else
    check "Config file is readable by current user" fail \
        "Hint: check ownership and permissions with ls -l"
fi

# Check 2: Is max_entries a valid number?
MAX=$(grep "^max_entries=" "$CONF" 2>/dev/null | cut -d= -f2)
if [[ "$MAX" =~ ^[0-9]+$ ]]; then
    check "max_entries is a valid number (e.g. 100)" pass
else
    check "max_entries is a valid number (e.g. 100)" fail \
        "Current value: '${MAX:-not found}'"
fi

# Check 3: Does the data_dir directory exist?
DATA_DIR=$(grep "^data_dir=" "$CONF" 2>/dev/null | cut -d= -f2)
if [ -n "$DATA_DIR" ] && [ -d "$DATA_DIR" ]; then
    check "data_dir directory exists ($DATA_DIR)" pass
else
    check "data_dir directory exists" fail \
        "Looking for: '${DATA_DIR:-not found in config}'"
fi

# Summary
echo ""
echo "------------------------------------------"
if [ "$FAIL" -eq 0 ]; then
    echo "  All $PASS checks passed. Configuration is valid."
else
    echo "  $PASS passed, $FAIL failed. Keep investigating."
fi
echo ""
