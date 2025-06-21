import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/help_desks.html')
def help_desks():
    return render_template('help_desks.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/feedback.html')
def feedback():
    return render_template("user_feedback.html")

@app.route('/profile.html')
def profile():
    return render_template("profile.html")

@app.route('/settings.html')
def settings():
    return render_template("settings.html")

@app.route('/notification.html')
def notification():
    return render_template("notification.html")

# Uncomment ini jika ingin akses file statis js firebase-config.js
# @app.route('/test-firebase')
# def test_firebase():
#     return app.send_static_file('js/firebase-config.js')

print("Templates folder contents:", os.listdir('templates'))


if __name__ == '__main__':
    app.run(debug=True)
