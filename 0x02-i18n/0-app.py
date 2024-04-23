#!/usr/bin/env python3
'''Set up basic flask app'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')
