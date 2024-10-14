import flask_login
from main.settings import main
from user_app.models import User


main.secret_key = "KEY"
login_manager = flask_login.LoginManager(app= main)
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)