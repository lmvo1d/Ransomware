from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

key = generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)
    