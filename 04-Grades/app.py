# imports
import datetime

from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import json
import datetime

# config
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'we live we love we lie'
moment = Moment(app)
date = datetime.datetime.now()

# load 'db'
with open("data/users.json") as f:
    users = json.load(f)

class LoginForm(FlaskForm):
    """
    formularz logowania
    """
    userLogin = StringField('Nazwa użytkowinka:', validators=[DataRequired()])
    userPass = PasswordField('Hasło:', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')



# routes
@app.route('/')
def index():
    loginForm = LoginForm()
    return render_template('index.html', title="Index", login=loginForm)

@app.route('/login', methods=['POST', 'GET'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        userLogin = loginForm.userLogin.data
        userPass = loginForm.userPass.data
        print(users)
        if userLogin == users['userLogin'] and userPass == users['userPass']:
            session['userLogin'] = userLogin
            session['firstName'] = users['firstName']
            return redirect('dashboard')
    return render_template('login.html', title="Logowaie", login=loginForm)

@app.route('/dashboard')
def dashboard():
    if not session.get('userLogin'):
        return redirect('login')
    return render_template('dashboard.html', title="Logowaie", userLogin=session.get('userLogin'), date=date)

@app.route('/logOut')
def logOut():
    if session.get('userLogin'):
        session.pop('userLogin')
    return redirect('login')


# run
if __name__ == "__main__":
    app.run(debug=True)
