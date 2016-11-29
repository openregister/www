#!/usr/bin/env python

import os

from flask import (
    Flask,
    render_template,
    redirect
)

from flask.ext.basicauth import BasicAuth
from flask.ext.cache import Cache

from get_registers import get_all_registers

app = Flask(__name__)
cache = Cache(app, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get("REDIS_URL", "redis://localhost:6379"),
})

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
    return redirect('/', 302)

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


phases = {
    'discovery': "discovery.openregister.org",
    'alpha': "alpha.openregister.org",
    'beta': "register.gov.uk"
}


@app.route("/registers")
@cache.cached(timeout=60*60*3)
def all_registers():
    registers = []
    for phase in phases:
        registers.append((phase, get_all_registers(phases[phase])))

    return render_template("list_of_registers.html", phase="All", registers=registers)


@app.route("/registers/<phase>")
@cache.cached(timeout=60*60*3)
def registers(phase):
    registers = []
    registers.append((phase, get_all_registers(phases[phase])))
    return render_template("list_of_registers.html", phase=phase, registers=registers)



if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get('PORT', '8002')),
        debug=True)
