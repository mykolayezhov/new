import flask

def render_home():
    
    if flask.request.method == "POST":
        if flask.request.form.get("send_recall"):
            name = flask.request.form.get("Name")
            email = flask.request.form.get("Email")
            recall_text = flask.request.form.get("recall_text")

    return flask.render_template("home.html")