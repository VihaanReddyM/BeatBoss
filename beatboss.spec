# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Custom helper to find ffmpeg and DLLs
import os
import glob

ffmpeg_files = []

# Find ffmpeg.exe
if os.path.exists("ffmpeg.exe"):
    ffmpeg_files.append(("ffmpeg.exe", "."))

# Find all FFmpeg DLL files
for dll in glob.glob("av*.dll") + glob.glob("sw*.dll") + glob.glob("postproc*.dll"):
    if os.path.exists(dll):
        ffmpeg_files.append((dll, "."))
    else:
        print(f"Warning: Redundant match for {dll}")

# Ensure ffmpeg.exe is included
if not any(f[0] == "ffmpeg.exe" for f in ffmpeg_files) and os.path.exists("ffmpeg.exe"):
    ffmpeg_files.append(("ffmpeg.exe", "."))

a = Analysis(
    ['main_build.py'],
    pathex=[],
    binaries=ffmpeg_files,
    datas=[('assets', 'assets')],
    hiddenimports=[
        'winrt.windows.foundation',
        'winrt.windows.foundation.collections',
        'winrt.windows.media',
        'winrt.windows.media.playback',
        'winrt.windows.storage.streams'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Add VLC bundle if it exists
vlc_tree = []
if os.path.exists('vlc'):
    vlc_tree = Tree('vlc', prefix='vlc')
    print("Found VLC folder - will be bundled with executable")

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
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon='assets/icon.ico' if os.path.exists('assets/icon.ico') else None
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    vlc_tree,  # Include bundled VLC folder
    strip=False,
    upx=False,
    upx_exclude=[],
    name='BeatBoss',
)
