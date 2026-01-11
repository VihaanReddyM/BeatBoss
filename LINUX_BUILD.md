# Linux Build Guide

This guide explains how to package BeatBoss as a standalone executable for Linux.

## Requirements

You must perform these steps on a Linux machine (Ubuntu/Debian recommended).

### 1. System Dependencies
Install the required system libraries for VLC and Python development:

```bash
sudo apt update
sudo apt install -y vlc libvlc-dev ffmpeg python3-pip python3-venv
```

### 2. Python Environment
Set up your virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flet python-vlc requests python-dotenv
```
*Note: Do not install `winrt` packages on Linux.*

## Building with PyInstaller

We can use PyInstaller to create a single-folder or single-file executable.

### 1. Simple Build
Run the following command in the project root:

```bash
pyinstaller --noconfirm --onedir --windowed \
    --add-data "assets:assets" \
    --name "BeatBoss" \
    main_flet.py
```

### 2. Using the Spec File
Since you have a Windows `.spec` file, you can create a simplified version for Linux (`beatboss_linux.spec`):

```python
# beatboss_linux.spec
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main_flet.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['winrt'], # Exclude Windows-specific modules
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BeatBoss',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon.png'], # Use PNG for Linux
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BeatBoss',
)
```

Build it using:
```bash
pyinstaller beatboss_linux.spec
```

## Distribution (AppImage)

The easiest way to share the app on Linux is an **AppImage**.

1. Download `appimagetool` from the AppImage GitHub.
2. Structure your folder:
   - `BeatBoss.AppDir/`
     - `usr/bin/` (put your compiled binary here)
     - `BeatBoss.desktop`
     - `icon.png`
     - `AppRun` (entry script)
3. Run `appimagetool BeatBoss.AppDir`.

## Limitations
*   System Media Controls: SMTC is Windows-only. On Linux, the app will function normally but won't show in the system volume mixer's media controls unless a Linux-specific library (like `mpris2`) is added later.
