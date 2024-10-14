import flask_sqlalchemy
import flask_migrate
import flask
import os





main = flask.Flask(import_name= 'main', template_folder= 'templates',instance_path=   os.path.abspath(__file__ + "/../.."+'/instance'))
main.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
DATABASE  = flask_sqlalchemy.SQLAlchemy(app = main)
MIGRATE = flask_migrate.Migrate(app=main , db= DATABASE)