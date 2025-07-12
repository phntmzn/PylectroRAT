

# Crypto utilities for PlectroRAT
# Provides AES encryption and decryption for secure communication and data handling

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'ThisIsASecretKey'  # Must be 16, 24, or 32 bytes long

def encrypt_data(data):
    """Encrypt data using AES and return base64-encoded ciphertext."""
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode("utf-8")
    ct = base64.b64encode(ct_bytes).decode("utf-8")
    return iv + ":" + ct

def decrypt_data(data):
    """Decrypt base64-encoded ciphertext using AES."""
    iv_str, ct_str = data.split(":")
    iv = base64.b64decode(iv_str)
    ct = base64.b64decode(ct_str)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode("utf-8")