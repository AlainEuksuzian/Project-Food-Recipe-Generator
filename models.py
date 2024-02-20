from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name= db.Column(db.String(64),index=True)
    last_name= db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    username= db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(256), index=True)
    gender = db.Column(db.String(20), index=True)
    food = db.relationship('Meal', backref='client', lazy='dynamic')

    def __repr__(self):
        return "<username: {u}; email:{e}; ".format(u=self.username,e=self.email)
    
    def generate_password(self, passwordInput):
        self.password_hash = generate_password_hash(passwordInput)
    
    def verify_password(self, passwordCheck):
        return check_password_hash(self.password_hash, passwordCheck)
    






class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    meal_category = db.Column(db.String(64), index=True)
    meal_area = db.Column(db.String(64), index=True)
    date_input = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<meal_category:{c}; area: {a}, >".format(c=self.meal_category, a=self.meal_area)
