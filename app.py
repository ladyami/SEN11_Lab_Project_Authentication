from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv  
import os  

# ============================================
# LOAD ENVIRONMENT VARIABLES
# ============================================
load_dotenv()  

app = Flask(__name__)

# ============================================
# SECRET KEY (from .env)
# ============================================
app.secret_key = os.getenv('SECRET_KEY')

# ============================================
# MySQL Configuration
# ============================================

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


# ============================================
# HOME ROUTE
# ============================================
@app.route('/')
def home():
    return render_template('index.html')

# ============================================
# SIGN UP ROUTE
# ============================================
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    # Clear any old flash messages before showing new ones
    session.pop('_flashes', None) 
    message = ""
    
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm = request.form['confirmPassword']
        
        # Validation
        if len(username) < 3:
            message = "❌ Username must be at least 3 characters!"
        elif password != confirm:
            message = "❌ Passwords do not match!"
        elif len(password) < 8:
            message = "❌ Password must be at least 8 characters!"
        else:
            # Check if username already exists
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM tbl_user WHERE username = %s", (username,))
            existing_user = cur.fetchone()
            
            if existing_user:
                message = "❌ Username already taken. Please choose another."
            else:
                # Hash password and save to database
                hashed_password = generate_password_hash(password)
                cur.execute(
                    "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
                    (username, hashed_password)
                )
                mysql.connection.commit()
                cur.close()
                
                session.pop('_flashes', None)  

                flash(f"✅ Account created successfully! Welcome {username}!")
                return redirect(url_for('signin'))
            
            cur.close()
    
    return render_template('signup.html', message=message)

# ============================================
# SIGN IN ROUTE
# ============================================
@app.route('/signin', methods=['GET', 'POST'])
def signin():

    
    error = None
    
    # If user is already logged in, redirect to dashboard
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        # Check if username exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tbl_user WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        
        
        if user and check_password_hash(user['password'], password):
            # Login successful - create session
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f"Welcome back, {user['username']}! 🎉")
            return redirect(url_for('dashboard'))
        else:
            error = "❌ Invalid username or password. Please try again."
    
    return render_template('signin.html', error=error)

# ============================================
# LOGOUT ROUTE
# ============================================
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out. See you soon! 👋")
    return redirect(url_for('signin'))

# ============================================
# DASHBOARD ROUTE 
# ============================================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please sign in to view your dashboard.")
        return redirect(url_for('signin'))
    
    # Get user info from database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_user WHERE id = %s", (session['user_id'],))
    user = cur.fetchone()
    cur.close()
    
    return render_template('dashboard.html', user=user)

# ============================================
# RUN APP
# ============================================
if __name__ == '__main__':
    app.run(debug=True)