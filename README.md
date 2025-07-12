


# PlectroRAT

PlectroRAT is a modular Remote Access Tool (RAT) built in Python for educational and research purposes. It provides functionality for remote command execution, keylogging, file access, and persistence across platforms.

## Features

- Remote shell access
- Keylogging
- Directory and file listing
- Screenshot capture
- AES-encrypted communication
- Windows/macOS persistence
- Flask-based command & control API
- Modular server/client architecture
- Cross-platform support

## Components

- `client.py` — Connects to the C2 server and executes commands
- `server.py` — Listens for incoming clients and routes commands
- `keylogger.py` — Captures keystrokes
- `screenshot.py` — Takes screenshots of the target's screen
- `crypto.py` — Handles AES encryption
- `shell.py` — Provides a remote shell interface
- `persistence.py` — Sets up autorun on Windows/macOS
- `api.py` — RESTful API for C2 management
- `handlers.py` — Handles client threading and command dispatch
- `logger.py` — Prints timestamped logs
- `connection.py` — Socket utility functions
- `scripts/` — Build and deployment scripts
- `tests/` — Unit tests for key modules

## Usage

1. Start the server:
   ```bash
   python3 server.py
   ```

2. Run the client on the target:
   ```bash
   python3 client.py
   ```

3. Use the Flask API:
   ```bash
   python3 api.py
   ```

4. Build and deploy:
   ```bash
   cd scripts
   ./build.sh
   ./deploy.sh
   ```

## Disclaimer

This tool is intended for **authorized research and educational use only**. Unauthorized deployment or usage may be illegal and is strictly discouraged.
