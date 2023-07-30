from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

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
    
if __name__ == '__main__':
    app.run(debug=True)