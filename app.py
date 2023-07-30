from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyBdcvTy_utP70utZwvBm6htsVefpDtqwi4",
  "authDomain": "ukko-project.firebaseapp.com",
  "projectId": "ukko-project",
  "storageBucket": "ukko-project.appspot.com",
  "messagingSenderId": "776487684222",
  "appId": "1:776487684222:web:efeffd3103adab1611b02f",
  "measurementId": "G-9YXEE9F93Z"
  "databaseURL": "https://ukko-project-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


# the code is down











# the code is up

f __name__ == '__main__':
    app.run(debug=True)