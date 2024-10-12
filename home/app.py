import flask

home_app = flask.Blueprint(
    name="home_app",
    import_name="home",
    template_folder="templates"
)