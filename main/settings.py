import flask
import flask_migrate
import flask_sqlalchemy
from flask_mail import Mail, Message


main = flask.Flask(
    import_name = 'main',
    template_folder= 'templates'
)


main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = flask_sqlalchemy.SQLAlchemy(main)
migrate = flask_migrate.Migrate(app = main, db = db)

main.config['MAIL_SERVER'] = 'smtp.gmail.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True
main.config["MAIL_USE_SSL"] = False


mail = Mail(main)
