#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''configure available languages in our app'''
    LANGUAGES = ["en", "fr"]
    # Configure the Babel object with the app
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''determines the best locale (language) to use for a given request'''
    # Get locale from query parameter
    locale = request.args.get('lang')
    if locale in app.config['LANGUAGES']:
        return locale
    # Get locale from user settings
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """renders a simple page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
