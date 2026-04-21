# 🔐 Password Manager CLI

A command-line password manager built with Python — focused on real-world backend logic, file handling, and practical CLI workflows.  
Built entirely on Termux (Android). No PC. No excuses.

---

## 🚀 Features

- Cryptographically secure password generation (`secrets`)
- Custom password length (user-controlled)
- Add and store passwords for different services
- View all saved passwords
- Delete passwords with confirmation
- Master key protection (access control before CLI)
- Persistent storage using JSON (file-based)
- Input validation & basic error handling
- Clean modular CLI structure

---

## 🛡️ Why `secrets` over `random`?

Most beginners use `random` for passwords — that’s unsafe.

- `random` → predictable (PRNG)  
- `secrets` → cryptographically secure (OS-level entropy)  

For any security-related functionality, `secrets` is the correct choice.

---

## ⚙️ Tech Stack

- Language: Python 3  
- Security: `secrets` module  
- Storage: JSON (file-based)  
- CLI Interface: Standard input/output  

---

## 📦 How to Run

```bash
git clone https://github.com/buildwith-krishna/password-manager-cli
cd password-manager-cli
python pass_gen.py
```

---

## 📋 CLI Flow

1. Enter master key (required to access system)

Then:

1. Password generator  
2. Add a password  
3. View all passwords  
4. Delete a password  
5. Exit  

---

## 🔐 Security Note

- Passwords are stored locally in `passwords.json`  
- Access is protected via a master key  
- Current version stores passwords in plain text (no encryption yet)  

---

## 🗺️ Roadmap

- [x] Password generator  
- [x] Add passwords  
- [x] Store passwords (JSON)  
- [x] View passwords  
- [x] Delete passwords  
- [x] Master key protection  
- [ ] Encrypt stored passwords  
- [ ] Hash master key  
- [ ] Search functionality  
- [ ] Category filtering  
- [ ] Database integration (SQLite)  
- [ ] GUI / Web version  

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)

> Building backend systems step by step with a focus on logic, structure,  
> and real-world usability — even in constrained environments.
