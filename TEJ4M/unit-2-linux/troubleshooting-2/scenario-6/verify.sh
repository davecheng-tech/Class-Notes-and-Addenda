#!/bin/bash
# =============================================================
# Scenario 6 — Media Server Verifier
# Run with: bash verify.sh
# =============================================================

SCRIPT=/usr/local/bin/rg-media
CONF=/etc/retrogames/media.conf
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
echo "=== RetroGames Media Server — Check ==="
echo ""

# Check 1: Is rg-media executable?
if [ -x "$SCRIPT" ]; then
    check "rg-media script is executable" pass
else
    check "rg-media script is executable" fail \
        "Hint: check permissions with ls -l $SCRIPT"
fi

# Check 2: Does the config file exist at the expected path?
if [ -r "$CONF" ]; then
    check "Config file exists and is readable at $CONF" pass
else
    check "Config file exists and is readable at $CONF" fail \
        "Hint: look at what is actually in /etc/retrogames/"
fi

# Check 3: Does the stream_dir directory exist?
STREAM_DIR=$(grep "^stream_dir=" "$CONF" 2>/dev/null | cut -d= -f2)
if [ -n "$STREAM_DIR" ] && [ -d "$STREAM_DIR" ]; then
    check "stream_dir directory exists ($STREAM_DIR)" pass
else
    check "stream_dir directory exists" fail \
        "${STREAM_DIR:+Looking for: '$STREAM_DIR'  — }${STREAM_DIR:-Check config path first: is the config file in the right place?}"
fi

# Summary
echo ""
echo "------------------------------------------"
if [ "$FAIL" -eq 0 ]; then
    echo "  All $PASS checks passed."
    echo "  Now run: rg-media"
else
    echo "  $PASS passed, $FAIL failed. Keep investigating."
fi
echo ""
