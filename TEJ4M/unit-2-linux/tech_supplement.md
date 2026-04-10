# Tech Supplement: Emulation Setup

This document covers setup details that will come up during the project. It will be updated as new questions come in.

## Contents

- [Getting ROMs: Classroom File Server](#getting-roms-classroom-file-server)
- [Getting ROMs: Google Drive](#getting-roms-google-drive)
- [ROM File Extensions](#rom-file-extensions)
- [Unzipping GBA ROMs](#unzipping-gba-roms)
- [Controllers](#controllers)
  - [Snes9x: Controller Not Responding](#snes9x-controller-not-responding)

---

## Getting ROMs: Classroom File Server

The classroom file server hosts ROM collections for NES, Game Boy, GBA, and SNES. The server's IP address is written on the board and may change between classes.

Two ways to connect: GUI (easier) or terminal.

### Method 1: Network Browser

**Step 1.** Open the **Network** icon from the desktop.

![Open the Network browser from the desktop](images/01.jpg)

**Step 2.** Click in the blank grey space at the top of the window to activate the address bar. Type the `smb://` address shown on the board, including the `/roms` share name.

![Click the address bar and enter the smb:// address](images/02.jpg)

> [!NOTE]
> The IP address shown here is an example. Use the address on the board — it will likely be different each class.

**Step 3.** When the Mount dialog appears, select **Connect as user** and enter the credentials. Leave Domain as `WORKGROUP`. Click **Connect**.

- **Username:** `student`
- **Password:** `student`

![Enter student / student and click Connect](images/03.jpg)

**Step 4.** The `roms` drive appears under **Devices** in the sidebar. Switch to **List View** for easier browsing. Copy the ROMs you want to your local machine before opening them in an emulator.

![The roms share mounted and browseable](images/04.jpg)

---

### Method 2: Terminal

Use this method if the GUI is not working, or if you prefer the command line.

**First time only — install the CIFS utility:**

```bash
sudo apt install cifs-utils
```

> [!IMPORTANT]
> If `apt` gives an error, you may not be authenticated on the school network. Open a browser and go to `http://connectme.ycdsb.ca` to log in first.

**First time only — create the mount point:**

```bash
sudo mkdir -p /mnt/roms
```

**Each session — mount the share** (use the IP address from the board):

```bash
sudo mount -t cifs //10.8.x.x/roms /mnt/roms -o username=student,ro
```

Enter `student` when prompted for a password.

ROMs are now available at `/mnt/roms`. You can browse them from the terminal with `ls /mnt/roms` or open them directly from an emulator's File > Open dialog.

> [!TIP]
> Only the mount command needs to be repeated each session. The `cifs-utils` install and `mkdir` steps are one-time only.

---

## Getting ROMs: Google Drive

A ROM collection is also available on the [classroom Google Drive share](https://drive.google.com/drive/folders/1CmMt-jrd8PWXR8gnmJWKtfcBfpMcjUl4). Download files directly to your machine.

---

## ROM File Extensions

| Extension | System |
|-----------|--------|
| `.nes` | Nintendo Entertainment System (NES) |
| `.gb` | Game Boy |
| `.gbc` | Game Boy Color |
| `.gba` | Game Boy Advance |
| `.sfc` | Super Nintendo / Super Famicom |

---

## Unzipping GBA ROMs

GBA ROMs on the class share are distributed as `.zip` files. You need to extract them before loading them into mGBA.

Right-click the `.zip` file in the file manager and choose **Extract Here**, or from the terminal:

```bash
unzip "ROM Name.zip"
```

This produces a `.gba` file in the same folder. Open that file in mGBA.

---

## Controllers

USB gamepads work in FCEUX and mGBA out of the box. Plug in your controller, open the emulator, and configure button mapping under the emulator's settings or preferences menu.

### Snes9x: Controller Not Responding

Snes9x is installed via snap, which sandboxes the application and blocks access to joystick devices by default. If your controller is not recognised in Snes9x's joypad configuration, run this once from the terminal:

```bash
sudo snap connect snes9x-gtk:joystick
```

Then restart Snes9x. Your controller should now appear and buttons can be mapped normally.

### Bluetooth

Bluetooth controller pairing on LXQt is possible but not covered here yet — check back if there's demand.
