import flask

tour_app = flask.Blueprint(
    name = "tour_app",
    import_name = "tour",
    template_folder= "templates",
    static_folder = "static",
    static_url_path = "/tour/"

)