#!/bin/bash
# =============================================================
# Scenario 3 — Configuration Verifier
# Run with: bash verify.sh
# =============================================================

CONF=/etc/retrogames/retrogames.conf
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
echo "=== RetroGames Configuration Verifier ==="
echo ""

# Check 1: Is the config file readable?
if [ -r "$CONF" ]; then
    check "Config file is readable by current user" pass
else
    check "Config file is readable by current user" fail \
        "Hint: check ownership and permissions with ls -l"
fi

# Check 2: Is log_level a valid value?
VALID_LEVELS="DEBUG INFO WARNING ERROR"
LOG_LEVEL=$(grep "^log_level=" "$CONF" 2>/dev/null | cut -d= -f2)
LEVEL_OK=fail
for level in $VALID_LEVELS; do
    if [ "$LOG_LEVEL" = "$level" ]; then
        LEVEL_OK=pass
        break
    fi
done
if [ "$LEVEL_OK" = "pass" ]; then
    check "log_level is a valid value (DEBUG / INFO / WARNING / ERROR)" pass
else
    check "log_level is a valid value (DEBUG / INFO / WARNING / ERROR)" fail \
        "Current value: '${LOG_LEVEL:-not found}'"
fi

# Check 3: Does the rom_path directory exist?
ROM_PATH=$(grep "^rom_path=" "$CONF" 2>/dev/null | cut -d= -f2)
if [ -n "$ROM_PATH" ] && [ -d "$ROM_PATH" ]; then
    check "rom_path directory exists ($ROM_PATH)" pass
else
    check "rom_path directory exists" fail \
        "Looking for: '${ROM_PATH:-not found in config}'"
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
