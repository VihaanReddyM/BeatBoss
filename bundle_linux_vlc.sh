#!/bin/bash

# BeatBoss VLC Bundler for Linux
# Run this before building with PyInstaller to bundle VLC with your app.

echo "Cleaning up old bundle..."
rm -rf vlc_libs
mkdir -p vlc_libs/lib
mkdir -p vlc_libs/plugins

echo "Copying VLC Libraries..."
# Try Debian/Ubuntu/Kali path first
if [ -d "/usr/lib/x86_64-linux-gnu" ]; then
    cp -v /usr/lib/x86_64-linux-gnu/libvlc.so* vlc_libs/lib/
    cp -v /usr/lib/x86_64-linux-gnu/libvlccore.so* vlc_libs/lib/
    
    echo "🔌 Copying Plugins..."
    cp -r /usr/lib/x86_64-linux-gnu/vlc/plugins/* vlc_libs/plugins/

# Try Arch/Fedora path
elif [ -f "/usr/lib/libvlc.so" ]; then
    cp -v /usr/lib/libvlc.so* vlc_libs/lib/
    cp -v /usr/lib/libvlccore.so* vlc_libs/lib/
    
    echo "Copying Plugins..."
    cp -r /usr/lib/vlc/plugins/* vlc_libs/plugins/

else
    echo "Error: Could not find VLC libraries! Make sure vlc is installed."
    exit 1
fi

echo "Done! 'vlc_libs' folder created."
echo "   Now run: python3 -m PyInstaller beatboss_linux.spec"
