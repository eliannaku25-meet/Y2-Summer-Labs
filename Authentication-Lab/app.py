from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="*******"


firebaseConfig = {
    "apiKey":"AIzaSyBSjFprdvxhVfWSEgdGUvlAbgylmKQkCWU",
    "authDomain":"authentificationproject-4939c.firebaseapp.com",
    "databaseURL":"https://authentificationproject-4939c-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId":"authentificationproject-4939c",
    "storageBucket":"authentificationproject-4939c.appspot.com",
    "messagingSenderId":"363635350388",
    "appId":"1:363635350388:web:aaa00e201e9ed520d7ea21",
    "measurementId": "G-GC8PC6HZG0",
    "databaseURL": "https://authentificationproject-4939c-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        quotes = []
        login_session['quotes']= quotes
        login_session.modified = True
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Womp it failed sad"
            return render_template("login.html", error=error)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        login_session.modifed= True
        return render_template("signup.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            print(login_session['user'])
            print(login_session['user']['localId'])
            login_session.modifed= True
            return redirect(url_for('home'))
        except:
            error = "Womp it failed. Try again"
            login_session.modifed= True
            return render_template("signup.html",error=error)
        
    
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    else:
        print("Made it to line 65!")
        login_session['quotes'].append(request.form['quote'])
        db.child("users").child(user_id).set({
            "user_quote": quote,
            })
        print(login_session['quotes'])
        login_session.modified= True
        return redirect(url_for('thanks'))


@app.route('/signout')
def signout():
    login_session['user']=None
    auth.current_user=None
    login_session.modified= True
    return redirect(url_for('login'))

@app.route('/thanks')
def thanks():
    login_session.modified= True
    return render_template('thanks.html')

@app.route('/display')
def display():
    quotes= db.child("users").child(user_id).child(user_id).get().val("user_quote": quote)
        

    login_session.modified = True
    return render_template('display.html',quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)
