import flask
from .models import User
from main.settings import DATABASE
import flask_login
def render_login():
    if flask.request.method == "POST":
        # for user in User.query.filter_by():
            
        #         flask_login.login_user(user)
        for user in User.query.filter_by(password = flask.request.form['password'],username = flask.request.form['username']):
            if user.password == flask.request.form['password']:
                if user.username == flask.request.form['username']:
                    flask_login.login_user(user)
    if flask_login.current_user.is_authenticated:
        return flask.redirect('/')

    
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
            return flask.redirect('/login')
        except Exception as error:
            print( error)

    return flask.render_template('registration.html')
