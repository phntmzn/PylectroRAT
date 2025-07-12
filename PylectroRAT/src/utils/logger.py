# Logger utility for PlectroRAT
# Provides simple logging functionality with timestamps

import datetime

def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] [{level.upper()}] {message}"
    print(formatted)
    return formatted

def log_error(message):
    return log(message, level="ERROR")

def log_success(message):
    return log(message, level="SUCCESS")

def log_warning(message):
    return log(message, level="WARNING")
