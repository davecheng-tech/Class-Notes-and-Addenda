# Reinstalling Lubuntu on an Acer C720 Chromebook

These machines already have MrChromebox coreboot firmware and a previous Lubuntu install. This guide walks through a clean reinstall using the class USB drive.

---

## Before You Start

1. Plug the Chromebook into an AC adapter. Do not run the installer on battery.
2. Get the class USB drive (it has Ventoy + the Lubuntu ISO loaded on it).

---

## Power On and Watch for the Boot Prompt

1. Insert the USB drive, then power on the Chromebook.
2. Watch for the **rabbit / coreboot logo** at the top of the screen during startup. When you see it, press **Esc** to open the boot menu.

> **Wrong logo?** If you see the **Chrome logo** (a white circle with coloured segments) instead, that machine still has the original Chromebook firmware and cannot run this process. Return it and get a different one.

---

## Select the Boot Device

1. From the boot menu, select **USB Removable** (may appear as `USB` or the drive's name).
2. Press **Enter** to boot from it.

---

## Ventoy — Choose the ISO

1. Ventoy loads and shows a list of ISOs on the drive.
2. Select the **Lubuntu ISO** and press **Enter**.
3. Choose **Normal Boot** and press **Enter**.

---

## Lubuntu Installer

1. Wait for Lubuntu to load to the desktop. This takes about a minute.
2. Double-click **Install Lubuntu** on the desktop, or click it in the taskbar.
3. Choose your language and click **Next**.
4. On the **Installation type** screen, select **Normal installation** and click **Next**.
5. On the **Disks** screen, select **Erase disk** and click **Next**.

   > This wipes the existing install and replaces it. That is the goal — do not choose any other option.

---

## User Account Setup

Fill in the following fields:

| Field | What to enter |
|-------|--------------|
| **Your name** | Your full name |
| **Login name** | A short, lowercase username (e.g., `jsmith`) — no spaces |
| **Computer name** | A name for this machine (e.g., `c720-01`) — no spaces |
| **Password** | Choose a password and confirm it |

Click **Next** when done.

---

## Wait and Finish

1. Review the summary screen and click **Install**.
2. The install takes roughly 10 minutes. You can watch the progress bar.
3. When finished, a dialog will prompt you to restart. Click **Restart Now**.
4. When the screen goes black and you see the prompt **Please remove the installation medium**, pull out the USB drive and press **Enter**.
5. The machine reboots into your fresh Lubuntu install.
