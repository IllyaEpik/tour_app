import flask 
import os
import flask_migrate
import flask_sqlalchemy

main = flask.Flask(import_name= 'main', template_folder= 'templates',instance_path=   os.path.abspath(__file__ + "/../.."+'/instance'))
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
data_base = flask_sqlalchemy.SQLAlchemy(app = main)
migrate = flask_migrate.Migrate(app = main, db = data_base)