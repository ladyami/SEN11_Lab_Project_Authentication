# SEN 311 Lab - Flask Authentication System

A secure web application built with Flask that features user authentication with password hashing, MySQL database integration, and a responsive Bootstrap 5 design with dark/light mode support.

## 🚀 Live Demo

[View Live Application](https://sen-11-lab-project-authentication.vercel.app/)

## 📋 Features

- **User Registration** - Create new accounts with password strength validation
- **User Login** - Secure authentication with session management
- **Password Hashing** - Passwords are hashed using Werkzeug before storage
- **MySQL Integration** - Remote database connection using PyMySQL
- **Dark/Light Mode** - Theme toggle with persistent preference storage
- **Responsive Design** - Bootstrap 5 with Miva University color palette
- **Dashboard** - User profile page after successful login
- **Session Management** - Secure logout functionality

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Flask** | Web framework |
| **PyMySQL** | MySQL database connector |
| **Werkzeug** | Password hashing |
| **Bootstrap 5** | Frontend styling |
| **Bootstrap Icons** | Icon library |
| **python-dotenv** | Environment variable management |
| **Vercel** | Deployment platform |
| **FreeDB** | Remote MySQL hosting |

## 📁 Project Structure

SEN11_Lab_Project/
│
├── app.py                 # Main Flask application (✅ MUST be in root)
├── requirements.txt       # Python dependencies (✅ MUST be in root)
├── vercel.json           # Vercel deployment config (✅ MUST be in root)
├── .env                  # Environment variables (✅ MUST be in root)
├── .gitignore            # Git ignore rules (✅ MUST be in root)
├── README.md             # Project documentation (✅ MUST be in root)
│
├── static/               # Static files folder (✅ MUST be at root level)
│   └── style.css         # Your custom CSS
│
└── templates/            # Template folder (✅ MUST be at root level)
    ├── index.html        # Homepage
    ├── signup.html       # Registration page
    ├── signin.html       # Login page
    └── dashboard.html    # User dashboard

## 🔧 Installation

### Prerequisites

- Python 3.10+
- MySQL database (local or remote)
- Git

### Local Setup

1. **Clone the repository:**
   
--bash
git clone https://github.com/YOUR_USERNAME/SEN11_Lab_Project.git
cd SEN11_Lab_Project

Create and activate a virtual environment:
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt


Create .env file:
SECRET_KEY=your-secret-key-here
MYSQL_HOST=sql.freedb.tech
MYSQL_USER=your_db_username
MYSQL_PASSWORD=your_db_password
MYSQL_DB=your_database_name

Set up database:
CREATE DATABASE your_database_name;
USE your_database_name;
CREATE TABLE tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Run the application:
python app.py


📝 License
This project is for educational purposes as part of SEN 311 - Web Application Development.

👤 Author
Student Name - Amina Oyegoke

Miva Open University

🙏 Acknowledgments
Miva Open University for the SEN 311 course

FreeDB for free MySQL hosting

Vercel for the deployment platform





## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Add comments for complex logic
- Keep HTML templates clean and readable

## Testing

- Test all routes locally before submitting
- Ensure dark/light mode works on all pages
- Verify database connections

## MIT License

Copyright (c) 2026 SEN 311 Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including, without limitation, the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

