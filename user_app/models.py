import flask
import flask_sqlalchemy
import flask_login
import main


class User(main.settings.DATABASE.Model, flask_login.UserMixin):
    id = main.settings.DATABASE.Column(main.settings.DATABASE.Integer, primary_key = True)
    username = main.settings.DATABASE.Column(main.settings.DATABASE.String(255))
    password =  main.settings.DATABASE.Column(main.settings.DATABASE.String(255))
    def __repr__(self) -> str:
        return f"username - {self.username}"