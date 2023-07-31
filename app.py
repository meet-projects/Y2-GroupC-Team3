from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {  
'apiKey': "AIzaSyC8obPXaGjAEb2L9z3SQlsl0ayJLGcB8do",
'authDomain': "nefashot-5fc6a.firebaseapp.com",
'projectId': "nefashot-5fc6a",
'storageBucket': "nefashot-5fc6a.appspot.com",
'messagingSenderId': "509898866148",
'appId': "1:509898866148:web:eed68f5761886822269bf1",
'measurementId': "G-ZZ8X71R5J8",
'databaseURL': 'https://nefashot-5fc6a-default-rtdb.europe-west1.firebasedatabase.app/'}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
#Code goes above here
@app.route('/sign_in', methods = ['POST','GET'])
def sign_in():
    erorr = ""
    if request.method == "POST":
        password = request.form['password']
        email = request.form['email']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {'password':password, 'email':email}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed  "
    
    return render_template("signin.html")

@app.route('/sign_up', methods = ['POST','GET'])
def sign_up():
    erorr = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {'name':name, 'name': name, 'email':email}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('home'))
        except:
          error = "Authentication failed  "
    return render_template("signup.html")

@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'POST':
        post = db.child("posts").get().val()
        return render_template('post.html', post = post)
    return render_template('post.html')

@app.route('/discuss', methods = ['GET', "POST"])
def discuss():
    if request.method == 'POST':
        try:
            name = request.form['name']
            upload = request.form['upload']
            about = request.form['about']
            contact = request.form['contact']
            post = {'name':name, 'upload': upload, 'about': about, 'contact': contact}
            db.child("Post").push(post)
            return redirect(url_for('post'))
        except: 
            return render_template('discuss.html')
    return render_template('discuss.html')
    
if __name__ == '__main__':
    app.run(debug=True)