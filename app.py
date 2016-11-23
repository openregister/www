#!/usr/bin/env python

import os

from flask import (
    Flask,
    render_template
)

from flask.ext.basicauth import BasicAuth
from get_registers import get_all_registers

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

@app.route("/alternative")
def alternative():
    return render_template("alternative.html")

@app.route("/benefits")
def benefits():
    return render_template("benefits.html")

@app.route("/running-registers")
def runningregisters():
    return render_template("running-registers.html")

@app.route("/using-registers")
def usingregisters():
    return render_template("using-registers.html")

@app.route("/composition-of-registers")
def compositionofregisters():
    return render_template("composition-of-registers.html")

@app.route("/modelling-register-data")
def modellingregisterdata():
    return render_template("modelling-register-data.html")

@app.route("/how-registers-work")
def howregisterswork():
    return render_template("how-registers-work.html")

@app.route("/developer")
def documentation():
    return render_template("developer.html")




@app.route("/list_of_registers")
def list_of_registers():
    registers = [
        ('discovery', get_all_registers("discovery.openregister.org")),
        ('alpha', get_all_registers("alpha.openregister.org")),
        ('beta', get_all_registers("beta.openregister.org")),
        ('live', get_all_registers("register.gov.uk")),

    ]

    return render_template("list_of_registers.html", registers=registers)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get('PORT', '8002')),
        debug=True)
