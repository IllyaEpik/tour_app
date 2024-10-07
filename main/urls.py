from .settings import main

import home_app
import tour_app
import user_app


main.add_url_rule(rule= '/', view_func= home_app.render_home)
main.add_url_rule(rule= '/tour/', view_func= tour_app.render_tour)
main.add_url_rule(rule= '/login/', view_func= user_app.render_login)
main.add_url_rule(rule= '/registration/', view_func= user_app.render_registration)

main.register_blueprint(home_app.home)
main.register_blueprint(user_app.user)
main.register_blueprint(tour_app.tour)