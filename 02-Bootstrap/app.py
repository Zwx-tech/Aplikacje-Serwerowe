# imports
from flask import Flask, render_template
from flask_bs4 import Bootstrap
# config
app = Flask(__name__)
bootstrap = Bootstrap(app)

# routes
@app.route('/')
def index():
    return render_template('index.html', title="Index")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internalServeError(e):
    return render_template("500.html"), 500
# run
if __name__ == "__main__":
    app.run(debug=True)
