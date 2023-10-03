# imports
from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired
import math

# config
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'we live we love we lie'

class LoginForm(FlaskForm):
    """
    formularz logowania
    """
    aField = IntegerField('a:', validators=[DataRequired()])
    bField = IntegerField('b:', validators=[DataRequired()])
    cField = IntegerField('c:', validators=[DataRequired()])
    submit = SubmitField('Solve')

# routes
@app.route('/')
def index():
    return render_template('index.html', title="Index")

@app.route('/solve', methods=['POST', 'GET'])
def login():
    loginForm = LoginForm()
    result = ''
    if loginForm.validate_on_submit():
        a = int(loginForm.aField.data)
        b = int(loginForm.bField.data)
        c = int(loginForm.cField.data)
        delta = b*b - 4*a*c
        if delta > 0:
            x1 = round((-b + math.sqrt(delta)) / (2 * a), 2)
            x2 = round((-b - math.sqrt(delta)) / (2 * a), 2)
            result = f'x1={x1}, x2={x2}'
        elif delta == 0:
            result = f'{round(-b / (2 * a), 2)}'
        else:
            result = 'brak miejsc zerowych'
    return render_template('login.html', title="Logowaie", login=loginForm, result=result)


# run
if __name__ == "__main__":
    app.run(debug=True)
