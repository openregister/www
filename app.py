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


@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
