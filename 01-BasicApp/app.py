# imports
from flask import Flask, render_template

# config
app = Flask(__name__)

@app.route('/template')
def template():
    return render_template('index.html', title="Template")

@app.route('/')
def index():
    return render_template('index.html', title="Index")

@app.route('/users')
def usersDeafult():
    return 'specify user'

@app.route('/users/<userName>')
def users(userName):
    return render_template('users.html', title="Users", userName=userName)

if __name__ == "__main__":
    app.run(debug=True)
