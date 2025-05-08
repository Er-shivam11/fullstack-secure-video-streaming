from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Fixed 16-byte key
KEY = b'MYSECRETKEY12345'

def encrypt_video(file_bytes):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    padded = pad(file_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return iv + encrypted  # Prepend IV

def decrypt_video(encrypted_bytes):
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size)
