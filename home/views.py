import flask
from main.models import DataRecall
from main.settings import mail
from flask_mail import Message

def render_home():
    if flask.request.method == "POST":
        if flask.request.form.get("recall"):
            name = flask.request.form.get("Name")
            email = flask.request.form.get("Email")
            recall_text = flask.request.form.get("recall_text")

            msg = Message(
                        subject= "Your order!",
                        recipients= 'mp8913969@gmail.com',
                        body = f'Клієнт {name} залишив/ла відгук:/n {recall_text}/n.Пошта для зворотнього звʼязку з клієнтом {email}.',
                        sender = [email]
                    )
           
            mail.send_message()
    return flask.render_template("home.html")
