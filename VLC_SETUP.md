# VLC Portable Setup Instructions

## Download VLC Portable

1. **Download**: https://get.videolan.org/vlc/3.0.21/win64/vlc-3.0.21-win64.zip (~80MB)

2. **Extract** the ZIP file

3. **Create folder** in your project:
   ```
   DAB-py/vlc/
   ```

4. **Copy contents**: Copy ALL files from the extracted VLC folder into `DAB-py/vlc/`

## Required Structure

After extraction, your `vlc/` folder should contain:
```
vlc/
├── vlc.exe
├── libvlc.dll
├── libvlccore.dll
└── plugins/
    └── (many .dll files)
```

## Testing

### Test 1: Local Development
```bash
cd DAB-py
python main_build.py
```

Look for console output: `[VLC] Using bundled VLC: ...`

### Test 2: Build Executable
```bash
clean_rebuild.bat
```

Check that `dist/BeatBoss/vlc/` folder exists with all VLC files.

### Test 3: Run Built App
1. Navigate to `dist/BeatBoss/`
2. Run `BeatBoss.exe`
3. Try playing a track
4. Verify audio works

## Verification

✅ **Success indicators:**
- Console shows "Using bundled VLC"
- Audio plays without errors
- App works on machines without VLC installed

❌ **Common issues:**
- Missing `libvlc.dll` - Didn't copy all files
- "VLC not found" - Wrong folder structure
- No audio - plugins/ folder missing

## Size Information

- VLC portable: ~80MB
- Final installer: ~120MB (vs ~40MB without VLC)
- Acceptable for a music player application
