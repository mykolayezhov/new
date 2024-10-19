import flask_sqlalchemy
import flask
from .settings import db





class DataRecall():
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    recall = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'recall {self.name}'
    


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def repr(self):
        return f'<User {self.username}>'
    
class Voucher(db.Model):
    # def __init__(self):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'voucher {self.id}'