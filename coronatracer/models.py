from .extensions import db
from flask_login import login_user, logout_user, login_required,UserMixin
class User(UserMixin,db.Model):
    id=db.Column(db.Integer)
    idapp=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60))
    password=db.Column(db.String(100))
    phone=db.Column(db.String(20))
    color=db.Column(db.String(10))
    contacts=db.Column(db.Text)
    time=db.Column(db.Text)
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.idapp

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


#from flask import Blueprint, render_template
#from .extensions import db
#from .models import User,Data
#import sqlite3
