import flask
import flask_login



def render_home():
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
    return flask.render_template('home.html', username= username)