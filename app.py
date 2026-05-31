from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey123"

bcrypt = Bcrypt(app)

# Database Setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home
@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome {session['user']} <br><a href='/logout'>Logout</a>"
    return redirect('/login')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        try:
            c.execute(
                "INSERT INTO users(username,password) VALUES (?,?)",
                (username, hashed_pw)
            )
            conn.commit()
            flash("Registration Successful")
            return redirect('/login')

        except:
            flash("Username already exists")

        conn.close()

    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = c.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session['user'] = username
            return redirect('/')

        flash("Invalid Username or Password")

    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
