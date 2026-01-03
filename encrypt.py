import os
from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file:
    key = key_file.read()

files = []

for file in os.listdir("."):
    if file in ["generate_key.py", "encrypt.py", "key.key", "decrypt.py", "README.md"]:
        continue

    files.append(file)

print("Encrypting files...")

for file in files:
    with open(file, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)

