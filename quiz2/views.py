#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello():
    # return "Hello Świat! <a href = http://127.0.0.1:5000/strona> strona </a>"
    return render_template("index.html")


@app.route("/lista")
def strona():
    return "<h1>Witaj na serwerze</h1><h2>Aplikacja Quiz</h2>"


@app.route("/klasa")
def klasa():
    return "<h1>Klasa 3a</h1>"
