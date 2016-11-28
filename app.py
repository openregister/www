#!/usr/bin/env python

import os

from flask import (
    Flask,
    render_template,
    redirect
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

@app.route("/demos")
def demos():
    return render_template("demos.html")

@app.route("/benefits")
def benefits():
    return redirect('/', 302)

@app.route("/running-registers")
def runningregisters():
    return redirect('/', 302)

@app.route("/using-registers")
def usingregisters():
    return redirect('/', 302)

@app.route("/composition-of-registers")
def compositionofregisters():
    return redirect('/', 302)

@app.route("/modelling-register-data")
def modellingregisterdata():
    return redirect('/', 302)

@app.route("/how-registers-work")
def howregisterswork():
    return redirect('/', 302)

@app.route("/developer")
def documentation():
    return redirect('/', 302)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', '8002')), debug=True)
