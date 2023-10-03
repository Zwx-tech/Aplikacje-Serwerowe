# imports
from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# config
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'we live we love we lie'

class LoginForm(FlaskForm):
    """
    formularz logowania
    """
    userLogin = StringField('Nazwa użytkowinka:', validators=[DataRequired()])
    userPass = PasswordField('Hasło:', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

users = {
    'userLogin': 'jjj',
    'userPass': 'zaq1',
    'firstName': 'Jan',
    'lastName': 'Wisz'
}
# routes
@app.route('/')
def index():
    return render_template('index.html', title="Index")

@app.route('/login', methods=['POST', 'GET'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        userLogin = loginForm.userLogin.data
        userPass = loginForm.userPass.data
        if userLogin == users['userLogin'] and userPass == users['userPass']:
            session['userLogin'] = userLogin
            return redirect('dashboard')
    return render_template('login.html', title="Logowaie", login=loginForm)

@app.route('/dashboard')
def dashboard():
    if not session.get('userLogin'):
        return redirect('login')
    return render_template('results.html', title="Logowaie", userLogin=session.get('userLogin'))

@app.route('/logOut')
def logOut():
    if session.get('userLogin'):
        session.pop('userLogin')
    return redirect('login')
# run
if __name__ == "__main__":
    app.run(debug=True)
