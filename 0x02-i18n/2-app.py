#!/usr/bin/env python3
'''Set up basic flask app'''

from flask import (
    Flask,
    render_template,
    request
    )
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.locale_selector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('1-index.html')
