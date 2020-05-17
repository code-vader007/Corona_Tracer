from flask import Blueprint, render_template
from .extensions import db
from .models import User,Data
import sqlite3

def add_user(id,name,password,phone):
    user=User(idapp=id,name=name,password=password,phone=phone)
    data=Data(idapp=id,color='G',contacts='',time='')
    db.session.add(user,data)
    db.commit()
def updatecontact(id1,id2):
    person=Data.query.filter_by(idapp=id1).first()
    k=person.contacts+str(id2)+" "
    person.contacts=k
    j=person.time+'0'+' '
    person.time=j
    db.session.commit()
def updatecolor(id,color):
    person=Data.query.filter_by(idapp=id).first()
    person.color=color
    db.session.commit()
def colorquery(id):
    person=Data.query.filter_by(idapp=id).first()
    c=person.color
    return c
def updatetime():
    users=Data.query.all()
    for user in users:
        k=user.time.rstrip().split(' ')
        for i in k:
            string=str(int(i)+1)
            k=k+string+' '
        user.time=k
    db.session.commit()
