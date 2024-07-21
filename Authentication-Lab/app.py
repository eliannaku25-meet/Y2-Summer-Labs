from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase

# App configuration
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

# Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyAr6GBfiEUoSs7PU1Iz6RsXY973W3mpW-8",
  "authDomain": "authlab-44360.firebaseapp.com",
  "projectId": "authlab-44360",
  "storageBucket": "authlab-44360.appspot.com",
  "messagingSenderId": "436236602790",
  "appId": "1:436236602790:web:253dfc8a1613048218d367",
  "measurementId": "G-LJ60N5MB83",
  "databaseURL": ""
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# App routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Login failed, try again."
            return render_template("login.html", error=error)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication error"
            return render_template("signup.html", error=error)

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        login_session['user'] = None
        return redirect(url_for('login'))

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        quote = request.form['quote']
        my_quotes = [quote]  # This is a simple implementation, normally you would store quotes in a database.
        return render_template("display.html", quote=my_quotes)
    return render_template("display.html", quote=[])

if __name__ == '__main__':
    app.run(debug=True)
