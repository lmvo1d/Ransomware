# 🔐 Ransomware / File Encryptor & Decryptor (Python)

A simple and secure **File Encryptor & Decryptor** built using **Python** and **Fernet symmetric encryption** from the `cryptography` library. This project allows users to encrypt files to protect sensitive data and decrypt them back safely using a secret key.

---

## ✨ Features

* 🔒 Strong symmetric encryption using **Fernet (AES + HMAC)**
* 📁 Encrypt any type of file (text, images, PDFs, etc.)
* 🔓 Decrypt files securely using the same key
* 🗝️ Automatic key generation and storage
* 🧑‍💻 Simple and beginner‑friendly Python implementation

---

## 🛠️ Technologies Used

* **Python 3.x**
* **cryptography** library (Fernet)

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/lmvo1d/ransomware.git
   cd file-encryptor-decryptor
   ```

2. **Install required dependency**

   ```bash
   pip install cryptography
   ```

---

## 🚀 Usage

### 1️⃣ Generate a Key

Run the key generation script:

```bash
python generate_key.py
```

This will create a `key.key` file. **Keep this file safe** — without it, decryption is impossible.

---

### 2️⃣ Encrypt a File

```bash
python encrypt.py
```

* Reads the file
* Encrypts it using the Fernet key
* Overwrites or creates an encrypted file (based on your implementation)

---

### 3️⃣ Decrypt a File

```bash
python decrypt.py
```

* Uses the same `key.key`
* Restores the original file securely

---

## 📂 Project Structure

```
ransomware/
│
├── generate_key.py        # Generates A Key
├── encrypt.py        # Encrypts the file
├── decrypt.py        # Decrypts the file
├── key.key           # Secret key (DO NOT SHARE)
└── README.md
```

---

## 🔐 How Fernet Encryption Works

* Uses **AES‑128** in CBC mode for encryption
* Uses **HMAC‑SHA256** for authentication
* Ensures **confidentiality + integrity** of data
* Same key is required for both encryption and decryption

---

## ⚠️ Important Notes

* ❗ Losing the `key.key` file means **permanent data loss**
* ❗ Never upload your encryption key to GitHub
* ✔️ Add `key.key` to `.gitignore`

```gitignore
key.key
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, improve the code, and submit a pull request.

---

## 👨‍💻 Author

**Anadi Sharma**
If you like this project, don’t forget to ⭐ the repository!

