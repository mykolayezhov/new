import flask_sqlalchemy
import flask
from .settings import db





class DataRecall():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    recall = db.Column(db.Text, nullable=False)




    def __repr__(self):
        return f'recall {self.name}'