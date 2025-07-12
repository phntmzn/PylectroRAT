

# Unit tests for connection.py module in PlectroRAT

import socket
import unittest
from unittest.mock import patch, MagicMock
from src import connection

class TestConnectionUtils(unittest.TestCase):

    @patch("socket.socket")
    def test_create_connection(self, mock_socket_class):
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance

        result = connection.create_connection("127.0.0.1", 4444)
        mock_socket_instance.connect.assert_called_with(("127.0.0.1", 4444))
        self.assertEqual(result, mock_socket_instance)

    def test_reliable_send(self):
        mock_socket = MagicMock()
        connection.reliable_send(mock_socket, "test message")
        mock_socket.sendall.assert_called_once_with(b"test message")

    def test_reliable_receive(self):
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b"received"
        result = connection.reliable_receive(mock_socket)
        self.assertEqual(result, "received")

if __name__ == "__main__":
    unittest.main()