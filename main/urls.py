import flask
import home
import tour
import user_app
from .settings import main

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.render_home,
    methods=['GET', 'POST']
)

tour.tour_app.add_url_rule(
    rule = "/tour/",
    view_func = tour.render_tour,
    methods=['GET', 'POST']
)
tour.tour_app.add_url_rule(
    rule = "/tour1/",
    view_func = tour.render_tour_page,
    methods=['GET', 'POST']
)


user_app.user_app.add_url_rule(
    rule = "/user/",
    view_func = user_app.render_user,
    methods=['GET', 'POST']
)
user_app.user_app.add_url_rule(
    rule = "/auth/",
    view_func = user_app.render_auth,
    methods=['GET', 'POST']
)


main.register_blueprint(blueprint=home.home_app)
main.register_blueprint(blueprint=user_app.user_app)
main.register_blueprint(blueprint=tour.tour_app)




