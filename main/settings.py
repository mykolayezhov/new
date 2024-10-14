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

main.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True
main.config['MAIL_USERNAME'] = 'your-email@example.com'
main.config['MAIL_PASSWORD'] = '12345678900tBig'
main.config['MAIL_DEFAULT_SENDER'] = 'travel.agency1462@gmail.com'

mail = Mail(main)
