import flask
import flask_login
from main.mail_config import ADMINISTRATION_ADRESS,mail
import flask_mail


def render_home():
    if flask.request.method == "POST":
        text = f"Клиент {flask.request.form['name']} оставил(а) отзыв: {flask.request.form['review']}.\n Почта для обратной связи с клиентом {flask.request.form['email']}."
        message = flask_mail.Message(
                    "Message Order",
                    sender= ADMINISTRATION_ADRESS, 
                    recipients= ['epi99k@gmail.com'], 
                    body= text
                )
        mail.send(message)
    username = None
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.username
    return flask.render_template('home.html', username= username)