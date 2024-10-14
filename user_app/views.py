import flask
from .models import User
from main.settings import DATABASE
def render_login():
    return flask.render_template('login.html')



def render_registration():
    if flask.request.method == "POST":
        print(flask.request.form)
        user = User(
                username = flask.request.form['username'],
                password = flask.request.form['password'],
                
            )
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
        except Exception as error:
            print( error)

    return flask.render_template('registration.html')
