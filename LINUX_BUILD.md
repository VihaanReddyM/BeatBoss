# Linux Build Guide & Setup

This guide explains how to set up the development environment and package BeatBoss as a standalone executable for Linux.

## 1. System Requirements

Unlike Windows, we rely on the system's package manager for media libraries.

### Install System Dependencies (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y vlc libvlc-dev ffmpeg libmpv-dev libmpv2 python3-pip python3-venv python3-tk
```
*   **vlc / libvlc-dev**: Required for the audio engine.
*   **ffmpeg**: Required for converting local files (WAV/MP3).
*   **libmpv-dev**: Required by Flet for its internal video components.

## 2. Python Environment Setup

Set up your virtual environment and install project dependencies.

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Install requirements
# Note: This will automatically skip Windows-only packages (winrt)
pip install -r requirements.txt
```

### Running the App Locally
```bash
python3 main_build.py
```

---

## 3. Building for Distribution (PyInstaller)

We use PyInstaller to create a standalone binary.

### Create the Linux Spec File (`beatboss_linux.spec`)

Save the following content as `beatboss_linux.spec` in the project root:

```python
# beatboss_linux.spec
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main_build.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['winrt', 'winrt.windows.media', 'windows_media'], # Exclude Windows modules
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
    console=False, # Set to True if you want to see debug logs in terminal
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/logo.png'], # Use PNG for Linux
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BeatBoss',
)
```

### Build the Application
```bash
pyinstaller beatboss_linux.spec
```

The output will be in `dist/BeatBoss/BeatBoss`.

## 4. Packaging as AppImage (Optional)

For a single-file portable executable that works on most Linux distros:

1.  Download **appimagetool** from GitHub.
2.  Create directory `BeatBoss.AppDir`.
3.  Copy directory `dist/BeatBoss` to `BeatBoss.AppDir/usr/bin`.
4.  Create `BeatBoss.desktop` and `AppRun` script.
5.  Run `appimagetool BeatBoss.AppDir`.
