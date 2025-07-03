# 🔐 Email & Password Validator API + UI

A simple Python Flask web application that validates user email and password input using custom rules. This includes a user-friendly web UI and an API-ready backend.

---

## 📌 Features

- ✅ Validates if **email** is exactly 6 characters long  
- ✅ Checks if **password** contains:
  - At least **1 uppercase letter**
  - At least **1 digit**
  - At least **1 special character**
- ✅ Ensures **password and confirm password** match
- ✅ Clean and responsive **HTML + CSS UI**
- ✅ Built using **Python Flask**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aditi2003hb/email-validator-api.git
cd email-validator-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
email-validator-api/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .gitattributes         # Ensures Python shows as main language on GitHub
│
├── templates/
│   └── index.html         # Frontend form UI
│
├── static/
│   └── style.css          # CSS styling
```

---

## 📡 API Endpoint (Optional)

You can also POST JSON to this endpoint directly:

- **URL:** `http://127.0.0.1:5000/validate`
- **Method:** `POST`
- **JSON Body Example:**

```json
{
  "email": "aditi1",
  "password": "Hello@123",
  "confirm_password": "Hello@123"
}
```

---

## ✅ Validation Rules

| Field             | Rule                                                                |
|------------------|----------------------------------------------------------------------|
| `email`           | Must be exactly 6 characters long                                   |
| `password`        | Must contain 1 uppercase, 1 digit, and 1 special character          |
| `confirm_password`| Must match the password                                             |

---

## ✨ Author

- GitHub: [@aditi2003hb](https://github.com/aditi2003hb)

---

## 📄 License

This project is licensed under the MIT License.

