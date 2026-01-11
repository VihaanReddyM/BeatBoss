# 🚀 How to Release BeatBoss on GitHub

**Note**: The automatic Git setup failed (internet/permissions error). You have two options:

## Option A: The Easy Way (Manual Upload)
1.  Go to `github.com/new` and create a repository.
2.  Click **"uploading an existing file"**.
3.  Drag and drop all files from this folder (except `.env`, `dist`, `Output`).
    *   ✅ Upload: `main_flet.py`, `settings.py`, `requirements.txt`, `assets/`, `license.txt`, `README.md`.
    *   ❌ BLOCK: `.env` (Secrets!), `dist/` (Too big), `Output/` (Too big).

## Option B: The Pro Way (Install Git)
1.  Download Git from [git-scm.com](https://git-scm.com/download/win).
2.  Install it (Next > Next > Finish).
3.  Open a new terminal and run:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
    git push -u origin main
    ```

---

## 🚀 Releasing the EXE (GitHub Releases)

Since you have a compiled application (`.exe`), you should use **GitHub Releases** to host it. This is better than just uploading the file to the code repository.

## Step 1: Push the Code
1.  Upload all your project files to your GitHub repository.
    *   **IMPORTANT**: Do NOT upload `.env` (it contains your secrets).
    *   Do upload `.env.example`.
    *   Do upload `.gitignore`.

## Step 2: Create a Release
1.  Go to your GitHub Repository page.
2.  Click **Releases** (usually on the right sidebar) -> **Draft a new release**.
3.  **Choose a Tag**: Type `v1.0.0` and click "Create new tag".
4.  **Title**: `BeatBoss v1.0.0 - Initial Release`.
5.  **Description**:
    ```markdown
    First official release of BeatBoss Player!
    
    ## Features
    - 🎵 Online Streaming
    - 📁 Local Playback
    - 📜 Auto-scrolling Lyrics
    - 🎨 Dark/Light Mode
    ```

## Step 3: Upload the Installer
1.  Look for the box that says **"Attach binaries by dropping them here"**.
2.  Drag and drop your **Installer** file:
    *   `Output\BeatBoss_Installer.exe`
3.  (Optional) You can also upload the standalone exe from `dist\BeatBoss\BeatBoss.exe` if you want a portable version.

## Step 4: Publish
Click **Publish release**. Now users can download your app directly from GitHub!
