# Finding Raspberry Pi IPs on the Network

Run from your Lubuntu Chromebook once Pis are powered on and have joined YCBYOD.
Pis must be imaged with hostnames pre-set (`rpi-01`, `rpi-02`, …) via Raspberry Pi Imager OS Customisation.

---

## Option A — nmap (filter by hostname)

```bash
sudo nmap -sn $(ip route | awk '/proto kernel/{print $1}' | head -1) | grep -A1 "rpi-"
```

The `ip route` subcommand auto-detects your subnet — no need to know `192.168.x.0/24` ahead of time. Output:

```
Nmap scan report for rpi-03.local (192.168.1.47)
Host is up (0.0038s latency).
```

**Filter by Raspberry Pi MAC vendor instead** (catches any Pi regardless of hostname):

```bash
sudo nmap -sn $(ip route | awk '/proto kernel/{print $1}' | head -1) | grep -B2 "Raspberry"
```

nmap identifies OUIs automatically and prints the IP line two above the vendor match.

---

## Option B — arp-scan (recommended)

Faster and cleaner output. One-time install:

```bash
sudo apt install arp-scan
```

Then:

```bash
sudo arp-scan --localnet | grep -i "raspberry"
```

Output:

```
192.168.1.45    dc:a6:32:1a:2b:3c    Raspberry Pi Trading Ltd
192.168.1.52    b8:27:eb:4d:5e:6f    Raspberry Pi Foundation
192.168.1.61    e4:5f:01:7a:8b:9c    Raspberry Pi Trading Ltd
```

IP, MAC, and vendor in one line. Completes in ~2 seconds. Easiest to paste into a Google Doc or Classroom announcement for students.

---

## Option C — mDNS (test this first)

If YCBYOD doesn't block multicast, avahi/mDNS works and is the cleanest option — no IP list needed at all.

Test from a student Chromebook:

```bash
ping rpi-01.local
```

If it resolves, students can SSH directly by name:

```bash
ssh pi@rpi-01.local
```

To discover all Pis at once:

```bash
avahi-browse -rt _ssh._tcp | grep "rpi-"
```

School BYOD networks often block multicast between devices. If `ping rpi-01.local` fails, fall back to Option A or B and use IPs.

---

## Raspberry Pi MAC OUI Reference

| MAC Prefix | Models |
|-----------|--------|
| `B8:27:EB` | Pi 1, 2, 3 |
| `DC:A6:32` | Pi 4 |
| `E4:5F:01` | Pi 5 |
| `28:CD:C1` | Pi 4 (some batches) |

---

## Day-of Workflow

1. Arrive early, power on all Pis
2. Wait ~45 seconds for boot and network join
3. Run arp-scan or nmap
4. Paste IP list into a Google Classroom announcement — one line per group: `rpi-03 → 192.168.1.47`
5. Test Option C (mDNS) from a student Chromebook while you wait — if it works, tell students to ignore the IP list and use `rpi-XX.local` directly
