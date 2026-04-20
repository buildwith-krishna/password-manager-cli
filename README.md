# 🔐 Password Manager CLI

A command-line password manager built with Python — focused on
security, clean architecture, and real-world usability.
Built entirely on Termux (Android). No PC. No excuses.

---

## 🚀 Features

- Cryptographically secure password generation
- Custom password length (user-controlled)
- Full input validation & error handling
- Clean modular structure

---

## 🛡️ Why `secrets` over `random`?

Most developers use `random` for password generation.
That's wrong.

`random` = predictable, pattern-based (PRNG)
`secrets` = OS-level entropy, cryptographically secure

For anything security-related, `secrets` is the only correct choice.

---

## ⚙️ Tech Stack

- Language: Python 3
- Security: `secrets` module
- Character sets: `string` module

---

## 📦 How to Run

git clone https://github.com/buildwith-krishna/password-manager-CLI
cd password-manager-CLI
python pass_gen.py

---

## 🗺️ Roadmap

- [x] Password generator
- [ ] Save passwords with encryption
- [ ] Retrieve saved passwords
- [ ] Master password protection
- [ ] Full CLI menu system

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)
> Building production-focused backend tools from scratch. On mobile.
