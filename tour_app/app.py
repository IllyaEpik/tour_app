import flask

tour = flask.Blueprint(name= "tour", import_name= "tour_app", template_folder= "templates", static_folder='static', static_url_path='/tour/')