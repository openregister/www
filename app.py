import os

from flask import (
    Flask,
    render_template
)

from flask.ext.basicauth import BasicAuth

app = Flask(__name__)

if os.environ.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
    app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_registers():
    return render_template("about.html")

@app.route("/demo")
def about():
    return render_template("demo.html")

@app.route("/developer")
def documentation():
    return render_template("developer.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', '8002')), debug=True)
