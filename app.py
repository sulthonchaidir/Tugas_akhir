from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/feedback')
def feedback():
    return render_template("user_feedback.html")

# @app.route('/test-firebase')
# def test_firebase():
#     return app.send_static_file('js/firebase-config.js')

if __name__ == '__main__':
    app.run(debug=True)
