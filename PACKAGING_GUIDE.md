# 📦 BeatBoss Packaging Guide (Zero to Hero)

This guide walks you through turning your Python code into a professional Windows Installer (`.exe`) that anyone can use.

## ✅ Prerequisites

1.  **FFmpeg**: Ensure `ffmpeg.exe` and `ffprobe.exe` are in your project folder (`DAB-py`).
2.  **Inno Setup**:
    *   **Download**: Go to [jrsoftware.org](https://jrsoftware.org/isdl.php) and download "Inno Setup 6.x.x".
    *   **Install**: Run the installer and click Next > Next > Finish.

---

## 🚀 Step 1: Build the App (PyInstaller)

This step bundles Python, VLC, and your code into a standalone folder.

1.  Open your **Terminal** (PowerShell or CMD) in the `DAB-py` folder.
2.  Run this command:
    ```powershell
    pyinstaller beatboss.spec
    ```
3.  **Wait**: It will take 1-2 minutes.
4.  **Verify**: You should see a new folder `dist\BeatBoss`.
    *   Open it and try running `BeatBoss.exe`.
    *   If it opens, you are ready for Step 2!

---

## 💿 Step 2: Create the Installer (Inno Setup)

This step takes the folder from Step 1 and compresses it into a single installer file (`BeatBoss_Installer.exe`).

1.  **Locate the Script**: Find `beatboss_installer.iss` in your project folder.
2.  **Open It**: Double-click `beatboss_installer.iss`. It should open in the "Inno Setup Compiler".
    *   *If asked "Do you want to create a new script?", say **Cancel** or **No**. You want to open the existing one.*
3.  **Compile**:
    *   Look at the top toolbar for a **Play Button (▶️)** or "Run" icon.
    *   Or, click **Build** menu -> **Compile**.
4.  **Wait**: You will see a green progress bar as it compresses files.
5.  **Success**: When finished, it might try to launch the installer to test it.

---

## 🎁 Phase 3: Distribution

1.  Go to your project folder (`DAB-py`).
2.  Open the `Output` folder (created by Inno Setup).
3.  You will see **`BeatBoss_Installer.exe`**.
    *   **This is the file you share with users.**
    *   They download it -> Double Click -> "I Agree" -> Install.
    *   It puts a shortcut on their Desktop and Start Menu.

---

## ❓ FAQ

**Q: Do users need Python?**
A: **No.** PyInstaller packed a mini-Python inside `BeatBoss.exe`.

**Q: Do users need VLC?**
A: **Maybe.** The installer checks for it! If they don't have it, it asks them to install it.

**Q: Does it save their login?**
A: **Yes.** The app saves settings to `%APPDATA%\BeatBoss`, which survives restarts and updates.
