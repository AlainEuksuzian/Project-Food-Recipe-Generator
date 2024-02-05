from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    food = db.relationship('Meal', backref='client', lazy='dynamic')

    def __repr__(self):
        return "<username: {u}; email:{e}; ".format(u=self.username,e=self.email)


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    meal_category = db.Column(db.String(64), index=True)
    meal_area = db.Column(db.String(64), index=True)
    date_input = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Relationship(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<meal_category:{c}; area: {a}, >"
