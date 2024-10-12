import flask, flask_migrate, flask_sqlalchemy

main = flask.Flask(
    import_name = 'main',
    template_folder= 'templates'
)
