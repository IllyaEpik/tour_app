import flask_mail
from .settings import main,DATABASE


ADMINISTRATION_ADRESS = "illyaepik@gmail.com"
ADMINISTRATION_PASSWORD = "eillya 2354"


main.config["MAIL_SERVER"] = 'smtp.gmail.com'
main.config["MAIL_PORT"] = 587
main.config["MAIL_USE_TLS"] = True
main.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
main.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
mail = flask_mail.Mail(app=main)