import flask
from main.models import User
from main.settings import db
def render_user():
   
    if flask.request.method == "POST":
        if flask.request.form.get("recall"):
            
            user = User(
                # id = flask.request.form.get("Id"),
                name = flask.request.form.get("Login"),
                password = flask.request.form.get("Password")
            )


            try:
                db.session.add(user)
                db.session.commit()
                return flask.redirect('/auth/')
            except:
                return 'Error'


    return flask.render_template(template_name_or_list = "user.html")

def render_auth():
    return flask.render_template(template_name_or_list = "auth.html")