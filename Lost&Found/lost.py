from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="*******"


firebaseConfig = {  
    "apiKey": "AIzaSyDA5G2lEmKiOFiup5ha-tfdQely23Q7Rto",
    "authDomain": "lost-and-found-665f2.firebaseapp.com",
    "projectId": "lost-and-found-665f2",
    "storageBucket": "lost-and-found-665f2.appspot.com",
    "messagingSenderId": "867865507512",
    "appId": "1:867865507512:web:ed9276d47451a13c78a64d",
    "measurementId": "G-69KTFNLTGT",
    "databaseURL": "https://lost-and-found-665f2-default-rtdb.europe-west1.firebasedatabase.app/"
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
        login_session.modified = True
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except Exception as e:
            error = "Womp it failed sad"
            print(e)
            return render_template("login.html", error=error)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        login_session.modifed= True
        return render_template("signup.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            login_session['user']= user
            user_id = user['localId']
            db.child("users").child(user_id).set({
                "name": name,
                "email": email
            })

            print(login_session['user'])
            print(login_session['user']['localId'])
            login_session.modifed= True
            return redirect(url_for('home'))
        except Exception as e:
            error = "Womp it failed. Try again"
            print(e)
            login_session.modifed= True
            return render_template("signup.html",error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        items={}
        return render_template("home.html",items = items)

@app.route('/signout')
def signout():
    login_session['user']=None
    auth.current_user=None
    login_session.modified= True
    return redirect(url_for('login'))

    
@app.route('/lost', methods=['GET', 'POST'])
def lost():
    if request.method=='GET':
        return render_template('lost.html')
    else:
            item = request.form['item']
            item_description = request.form['item-description']
            last_seen = request.form['last-seen']
            user_id = login_session['user']['localId']
            db.child("items").push({
                    "item" : item,
                    "item_description" : item_description,
                    "last_seen" : last_seen,
                    "owner": user_id
                    })
            user_id = login_session['user']['localId']
            items = db.child("items").get().val()
            print(items)
            return render_template("home.html", items=items)

@app.route('/contact<owner>', methods=['GET', 'POST'])
def contact(owner):
    if request.method=='GET':
        owner_profile = db.child("users").child(owner).get().val()
        return render_template('contact.html', user=owner_profile)

        
if __name__ == '__main__':
    app.run(debug=True)
