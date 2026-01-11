# Windows Media Integration Setup

## Required Package

To enable Windows system media controls (taskbar controls, headphone buttons, cover art display), you need to install the Windows Runtime package:

```bash
pip install winrt
```

## What This Enables

Once installed, the app will automatically integrate with Windows:

### ✅ System Media Controls
- **Taskbar Controls**: Play/pause, next, previous buttons in Windows taskbar
- **Media Overlay**: Shows track info and cover art in Windows media overlay (Win + Alt + B)
- **Lock Screen**: Track info and controls on Windows lock screen
- **Headphone Buttons**: Control playback with headphone/keyboard media keys

### ✅ Cover Art Display
- Album artwork appears in:
  - Windows taskbar media controls
  - Windows media overlay
  - Lock screen
  - Bluetooth device displays (if supported)

### ✅ Track Metadata
- Song title
- Artist name
- Album name (if available)
- Album artwork

## How It Works

The app uses Windows System Media Transport Controls (SMTC) API through the `winrt` package to:
1. Register as a media player with Windows
2. Update metadata when tracks change
3. Sync playback status (playing/paused)
4. Handle media button presses from any source

## Fallback Behavior

If `winrt` is not installed:
- App will still work normally
- Keyboard media keys will still work (via pynput)
- Windows system integration will be disabled
- Console will show: `[SMTC] Windows Runtime not available`

## Installation

```bash
# Install the package
pip install winrt

# Restart the app
python main_flet.py
```

You should see in the console:
```
[SMTC] Windows media controls initialized successfully
```

Then when you play a track:
```
[SMTC] Updated metadata: Track Title - Artist Name
[SMTC] Playback status: Playing
```
