import flask

def render_personalization():
    color_0 = "blue"
    return flask.render_template("personalization.html" , color_0= color_0)