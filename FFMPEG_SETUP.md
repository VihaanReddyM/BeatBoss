# FFmpeg Setup for Local Playback

## Why FFmpeg?

VLC's Python bindings have compatibility issues with certain MP3 encodings. FFmpeg solves this by:
1. Decoding the MP3 file
2. Converting to PCM WAV format
3. Piping the audio stream to VLC
4. VLC plays the stream perfectly

## Installation

### Windows (using winget):
```bash
winget install ffmpeg
```

### Or download manually:
1. Download from: https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg\`
3. Add `C:\ffmpeg\bin\` to PATH

### Verify installation:
```bash
ffmpeg -version
```

## How It Works

**For Local Files**:
```
MP3 File → FFmpeg (decode) → WAV Stream → VLC (play)
```

**For Streaming**:
```
HTTP Stream → VLC (direct playback)
```

## What You'll See

When playing a downloaded track:
```
[FFmpeg→VLC] Playing: Naal Nachna.mp3
[FFmpeg→VLC] ✓ Playback started
```

When streaming:
```
[VLC] Loading: https://...
[VLC] ✓ Playback started
```

## Fallback

If ffmpeg is not installed:
- App will show: `[FFmpeg] ERROR: ffmpeg not found`
- Falls back to direct VLC playback (may not work for all MP3s)
- Streaming will still work normally
