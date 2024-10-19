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


            try:
                msg = Message(
                            subject= "Your order!",
                            recipients = ["mykolayezhov@gmail.com"],
                            body = f'Клієнт {name} залишив/ла відгук: {recall_text}. Пошта для зворотнього звʼязку з клієнтом {email}.',
                            sender = email
                        )
                # print(msg.recipients)
                mail.send(msg)


            except Exception as e:
                print(f"mail-send-error: {e}")


                
    return flask.render_template("home.html")
