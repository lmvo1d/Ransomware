import os
from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()

    return key


key = load_key()
files = []
code = input("Enter decryption code : ")

if code == "404NotFound":
    print("Code accepted")

    for file in os.listdir("."):
        if file in ["generate_key.py", "encrypt.py", "key.key", "decrypt.py", "README.md"]:
            continue

        files.append(file)

    print("Decrypting files...")

    for file in files:
        with open(file, "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open(file, "wb") as f:
            f.write(decrypted)

else:
    print("Invalid code! Exiting...")

