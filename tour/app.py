import flask

tour_app = flask.Blueprint(
    name = "tour_app",
    import_name = "tour",
    template_folder= "templates"
)