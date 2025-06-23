# 🗂️ File Information Explorer

A beginner-friendly Python project to explore directories from the terminal. Built using only Python's standard library. This is part of my learning journey in mastering file systems, directories, regex, and automation with Python.

---

## 🚀 Features

- Show files, folders, or both in any directory
- Display file name, size, and last modified date
- Navigate using relative/absolute paths
- Uses `os`, `glob`, and `datetime`
- Bonus: Includes regex-based email & password validation (signup/login system)

---

## 🛠 Technologies Used

- Python 3
- `os`
- `os.path`
- `os.scandir()`, `os.stat()`
- `datetime.fromtimestamp()`
- `glob`
- `re` (Regex)

---

## 🔐 Regex for Validation

- **Email Regex:**
  ```python
  r"^[\w\.-]+@[\w\.-]+\.\w+$"
**password:** 
r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$"
