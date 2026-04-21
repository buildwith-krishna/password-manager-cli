# 🔐 Password Manager CLI

A command-line password manager built with Python — focused on
real-world backend logic, data handling, and practical usability.
Built entirely on Termux (Android). No PC. No excuses.

---

## 🚀 Features

- Cryptographically secure password generation
- Custom password length (user-controlled)
- Add and store passwords for different services
- View saved passwords (protected by master key)
- Persistent storage using JSON (file-based)
- Full input validation & error handling
- Clean modular CLI structure

---

## 🛡️ Why `secrets` over `random`?

Most developers use `random` for password generation.
That's incorrect for security use-cases.

`random` → predictable (PRNG)  
`secrets` → OS-level entropy, cryptographically secure  

For password generation, `secrets` is the correct choice.

---

## ⚙️ Tech Stack

- Language: Python 3
- Security: `secrets` module
- Storage: JSON (file-based database)
- CLI Interaction: Standard input/output

---

## 📦 How to Run

git clone https://github.com/buildwith-krishna/password-manager-cli  
cd password-manager-cli  
python pass_gen.py  

---

## 📋 CLI Menu

1. Password generator  
2. Add a password  
3. View all passwords  
4. Exit  

---

## 🔐 Security Note

- Passwords are stored locally in a JSON file
- Access is restricted using a master key
- Current version does NOT use encryption (planned improvement)

---

## 🗺️ Roadmap

- [x] Password generator
- [x] Add a password(JSON)
- [x] Store passwords (JSON)
- [x] View passwords (master key protected)
- [ ] Encrypt stored passwords
- [ ] Hash master key
- [ ] Update/Delete password functionality
- [ ] Export data (CSV/Excel)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] GUI / Web version

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)

> Building backend systems from scratch with a focus on logic,
> structure, and real-world problem solving — even in constrained environments.
