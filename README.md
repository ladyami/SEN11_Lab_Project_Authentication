# SEN 311 Lab - Flask Authentication System

A secure web application built with **Flask** that features user authentication, password hashing, MySQL database integration, and a responsive **Bootstrap 5** interface with dark/light mode support.

## 🚀 Live Demo

🔗 https://sen-11-lab-project-authentication.vercel.app/

---

## 📋 Features

- 🔐 User Registration with password validation
- 🔑 Secure User Login with session management
- 🛡️ Password Hashing using Werkzeug
- 🗄️ MySQL Database Integration
- 🌙 Dark & Light Mode with saved user preference
- 📱 Responsive Bootstrap 5 UI
- 👤 User Dashboard
- 🚪 Secure Logout
- ☁️ Deployed on Vercel

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Flask | Web Framework |
| PyMySQL | MySQL Database Connector |
| Werkzeug | Password Hashing |
| Bootstrap 5 | Frontend Styling |
| Bootstrap Icons | Icons |
| python-dotenv | Environment Variables |
| MySQL | Database |
| FreeDB | Remote MySQL Hosting |
| Vercel | Deployment |

---

# 📁 Project Structure

```text
SEN11_Lab_Project/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel configuration
├── .env                    # Environment variables
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── signup.html
    ├── signin.html
    └── dashboard.html
```

---

# 🔧 Installation

## Prerequisites

- Python 3.10+
- Git
- MySQL Database (Local or Remote)

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SEN11_Lab_Project.git

cd SEN11_Lab_Project
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key-here

MYSQL_HOST=sql.freedb.tech
MYSQL_USER=your_db_username
MYSQL_PASSWORD=your_db_password
MYSQL_DB=your_database_name
```

---

## Create the Database

```sql
CREATE DATABASE your_database_name;

USE your_database_name;

CREATE TABLE tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🚀 Deployment

The project is deployed on **Vercel**.

Live URL:

https://sen-11-lab-project-authentication.vercel.app/

---



---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

# 🧪 Testing

Before deployment, ensure that:

- User registration works
- Login authentication works
- Passwords are hashed
- Dashboard loads after login
- Logout clears the session
- Dark/Light mode works correctly
- Database connection is successful

---

# 📖 Code Style

- Follow **PEP 8**
- Keep functions small and readable
- Add comments where necessary
- Keep HTML templates organized

---

# 👨‍💻 Author

**Amina Oyegoke**

Software Engineering Student  
Miva Open University

---

# 🙏 Acknowledgments

- Miva Open University
- SEN 311 – Web Application Development
- Flask Documentation
- Bootstrap
- FreeDB
- Vercel

---

# 📄 License

MIT License

Copyright (c) 2026 Amina Oyegoke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
