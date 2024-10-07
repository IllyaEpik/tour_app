import flask

def render_login():
    return flask.render_template('login.html')

def render_registration():
    return flask.render_template('registration.html')