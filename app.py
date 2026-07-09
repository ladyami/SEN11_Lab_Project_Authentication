from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import pymysql
from pymysql.cursors import DictCursor
import sys

# ============================================
# LOAD ENVIRONMENT VARIABLES
# ============================================
load_dotenv()

app = Flask(__name__)

# ============================================
# SECRET KEY (from .env)
# ============================================
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key-for-dev')

# ============================================
# DATABASE CONNECTION FUNCTION
# ============================================
def get_db_connection():
    """Create and return a database connection using PyMySQL."""
    try:
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DB', 'flask_db'),
            cursorclass=DictCursor,
             ssl=None,
            connect_timeout=10  #  timeout
        )
        return connection
    except Exception as e:
        print(f"❌ Database connection error: {str(e)}", file=sys.stderr)
        raise

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
    # Clear any old flash messages
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
            try:
                # Get database connection
                connection = get_db_connection()
                try:
                    with connection.cursor() as cur:
                        # Check if username already exists
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
                            connection.commit()
                            
                            session.pop('_flashes', None)
                            flash(f"✅ Account created successfully! Welcome {username}!")
                            return redirect(url_for('signin'))
                except Exception as e:
                    print(f"❌ Database query error: {str(e)}", file=sys.stderr)
                    message = f"❌ Database error: {str(e)}"
                finally:
                    connection.close()
            except Exception as e:
                print(f"❌ Connection error: {str(e)}", file=sys.stderr)
                message = "❌ Could not connect to database. Please try again later."
    
    return render_template('signup.html', message=message)

# ============================================
# SIGN IN ROUTE
# ============================================
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        session.pop('_flashes', None)
        username = request.form['username'].strip()
        password = request.form['password']
        
        try:
            connection = get_db_connection()
            try:
                with connection.cursor() as cur:
                    cur.execute("SELECT * FROM tbl_user WHERE username = %s", (username,))
                    user = cur.fetchone()
                    
                    if user and check_password_hash(user['password'], password):
                        session['user_id'] = user['id']
                        session['username'] = user['username']
                        flash(f"Welcome back, {user['username']}! 🎉")
                        return redirect(url_for('dashboard'))
                    else:
                        error = "❌ Invalid username or password. Please try again."
            except Exception as e:
                print(f"❌ Database query error: {str(e)}", file=sys.stderr)
                error = "❌ Database error. Please try again."
            finally:
                connection.close()
        except Exception as e:
            print(f"❌ Connection error: {str(e)}", file=sys.stderr)
            error = "❌ Could not connect to database. Please try again later."
    
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
    
    try:
        connection = get_db_connection()
        try:
            with connection.cursor() as cur:
                cur.execute("SELECT * FROM tbl_user WHERE id = %s", (session['user_id'],))
                user = cur.fetchone()
                return render_template('dashboard.html', user=user)
        except Exception as e:
            print(f"❌ Dashboard query error: {str(e)}", file=sys.stderr)
            flash("❌ Could not load dashboard. Please try again.")
            return redirect(url_for('home'))
        finally:
            connection.close()
    except Exception as e:
        print(f"❌ Connection error: {str(e)}", file=sys.stderr)
        flash("❌ Could not connect to database. Please try again later.")
        return redirect(url_for('home'))


@app.route('/test-db')
def test_db():
    try:
        connection = get_db_connection()
        with connection.cursor() as cur:
            cur.execute("SELECT 1")
            result = cur.fetchone()
        connection.close()
        return "✅ Database connection successful!"
    except Exception as e:
        return f"❌ Database connection failed: {str(e)}"
# ============================================
# RUN APP
# ============================================
if __name__ == '__main__':
    app.run(debug=True)