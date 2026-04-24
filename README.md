# 🔐 Password Manager CLI

> A fully encrypted, command-line password manager built in Python — from scratch, on a phone.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS-green?style=flat-square)
![Security](https://img.shields.io/badge/Encryption-Fernet%20AES--128-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

Built entirely on **Termux (Android)**. No PC. No excuses.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔑 **Master Key Auth** | 3-attempt lockout system before access is granted |
| 🔒 **Fernet Encryption** | All passwords encrypted at rest using AES-128 |
| 🎲 **Secure Generator** | Cryptographically secure passwords via `secrets` module |
| 📁 **Persistent Storage** | JSON file-based storage with clean structure |
| ➕ **Add** | Store credentials for any service |
| 👁️ **View** | Display all saved passwords (decrypted on-the-fly) |
| 🗑️ **Delete** | Remove entries with confirmation prompt |
| ✏️ **Update** | Modify existing credentials |
| 🔍 **Search** | Find passwords instantly by service name |
| ✅ **Input Validation** | Handles empty fields and invalid inputs gracefully |

---

## 🛡️ Security Design

### Encryption
Every password is encrypted before being written to disk using **Fernet symmetric encryption** from the `cryptography` library:

```
User Password → f.encrypt() → Encrypted blob stored in JSON
Encrypted blob → f.decrypt() → Original password shown to user
```

The Fernet key is derived from your master key at runtime using **SHA-256 hashing** — meaning nothing sensitive is ever stored anywhere.

### Why `secrets` over `random`?

| | `random` | `secrets` |
|---|---|---|
| Type | Pseudo-random (PRNG) | Cryptographically secure |
| Source | Algorithm-based | OS-level entropy |
| Safe for passwords? | ❌ | ✅ |

### Master Key Lockout
3 failed attempts → program exits. No brute force.

---

## ⚙️ Tech Stack

- **Language** — Python 3
- **Encryption** — `cryptography` (Fernet / AES-128)
- **Password Generation** — `secrets` + `string`
- **Storage** — JSON (file-based, local)
- **Interface** — CLI (standard input/output)

---

## 📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/buildwith-krishna/password-manager-cli

# Navigate into the project
cd password-manager-cli

# Install dependency
pip install cryptography

# Run
python pass_gen.py
```

---

## 🖥️ CLI Flow

```
Enter master key: ••••••••••••••

## Password_Manager ##
1. Password generator
2. Add a password
3. View all passwords
4. Delete a password
5. Update a password
6. Search a password
7. Exit
```

---

## 📁 Project Structure

```
password-manager-cli/
├── pass_gen.py       # Main application
├── passwords.json    # Encrypted password storage (auto-created)
└── README.md
```

---

## ✅ Completed Scope

- [x] Cryptographically secure password generator
- [x] Add / View / Delete / Update / Search passwords
- [x] JSON-based persistent storage
- [x] Master key authentication
- [x] 3-attempt lockout on wrong master key
- [x] Fernet encryption on all stored passwords
- [x] SHA-256 key derivation from master key
- [x] Input validation and error handling
- [x] Clean modular code structure

**This project is complete as designed.**

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)

> *"Building backend systems step by step — with focus on logic, structure, and real-world usability. Even from a phone."*
