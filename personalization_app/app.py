import flask

personalization = flask.Blueprint(
                                  name="personalization", 
                                  import_name="personalization_app", 
                                  template_folder="templates", 
                                  static_folder="static", 
                                  static_url_path="/personal/"
)