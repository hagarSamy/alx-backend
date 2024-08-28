#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
import datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''configure available languages in our app'''
    LANGUAGES = ["en", "fr"]
    # Configure the Babel object with the app
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''determines the best locale (language) to use for a given request'''
    # detects if the incoming request contains locale argument
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Get locale from user settings
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    '''returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed'''
    return users.get(user_id)


@app.before_request
def before_request():
    '''use get_user to find a user if any,
    and set it as a global on flask.g.user'''
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    '''determines the time zone to use for a given request'''
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass  # If invalid, continue to check the user settings
    if g.user.get('timezone'):
        timezone = g.user.get('timezone')
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """renders html page"""
    current_time = datetime.datetime.now()
    formatted_time = format_datetime(current_time, format='medium')
    return render_template('index.html', current_time=formatted_time)


if __name__ == '__main__':
    app.run(debug=True)
