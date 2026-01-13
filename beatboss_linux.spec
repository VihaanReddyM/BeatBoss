# beatboss_linux.spec
# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

# Dynamic Configuration
# ---------------------
my_datas = [('assets', 'assets')]
my_binaries = []

# Check if user ran the bundle script
if os.path.exists('vlc_libs'):
    print("📦 Found bundled 'vlc_libs' folder! Including it in the build...")
    my_datas.append(('vlc_libs', 'vlc_libs'))
else:
    print("⚠️ No 'vlc_libs' folder found. Using System VLC (must be installed on target machine).")
    # If not bundling, we rely on player.py's dynamic discovery via ldconfig

a = Analysis(
    ['main_build.py'],
    pathex=[],
    binaries=my_binaries,
    datas=my_datas,
    hiddenimports=['flet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['winrt', 'winrt.windows.media'], # Exclude Windows-specific libs
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

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
    console=True, # Set to False for production (hides terminal)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/logo.png'],
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
