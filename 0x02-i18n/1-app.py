#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    '''configure available languages in our app'''
    LANGUAGES = ["en", "fr"]
    # Configure the Babel object with the app
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """renders a simple page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
