import flask
from .models import User
from main.settings import DATABASE
import flask_login
def render_login():
    add = ""
    if flask.request.method == "POST":
        # for user in User.query.filter_by():
            
        #         flask_login.login_user(user)
        for user in User.query.all():
            add = ""
            # print(user.username == flask.request.form['username'],user.password == flask.request.form['password'])
            if user.username == flask.request.form['username']:
                if user.password == flask.request.form['password']:
                    flask_login.login_user(user)
                    return flask.redirect('/')
                else:
                    add= "Невірний пароль"
                    break
            else:
                add="Невірне імя користувача"
        if not len(User.query.all()):
            return flask.redirect('/registration')
    username = None
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
    # print(add)
    return flask.render_template('login.html',username=username, add=add)
def render_logout():
    flask_login.logout_user()
    return flask.redirect('/')



def render_registration():
    add = ""
    if flask.request.method == "POST":
        all_is_ok = True
        for login in User.query.all():
            if login.username == flask.request.form['username']:
                all_is_ok= False
        if all_is_ok:

            
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
        else:
            add = "Вибачте це імя користувача вже використувано"
    username = None
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
    return flask.render_template('registration.html', username=username, add = add)
