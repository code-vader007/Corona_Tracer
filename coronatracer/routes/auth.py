from flask import Blueprint, render_template, redirect, url_for, request,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,UserMixin
from coronatracer.extensions import db
from coronatracer.models import User

import sqlite3

auth=Blueprint('auth',__name__)
@auth.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        name=request.form["Username"]
        idapp=int(request.form["Appid"])
        phone=request.form["phone"]
        pwsd=request.form["password"]
        pwsd2=request.form["password2"]
        person=User.query.filter_by(idapp=idapp).first()
        if(pwsd!=pwsd2):
            flash('The passwords donot match.Please check again','error')
            return redirect(url_for('auth.signup'))
        if(person!=None):
            flash('There is already a person with the same id number.Select a different id','error')
            return redirect(url_for('auth.signup'))
        else:
            user=User(idapp=idapp,name=name,password=generate_password_hash(pwsd),phone=phone,color='G',contacts='',time='')
            db.session.add(user)
            db.session.commit()
            flash('You have signed up succesfully','info')
            return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')
@auth.route('/login',methods=["POST","GET"])
def login():
    if request.method=='POST':
        idapp=request.form["id"]
        password=request.form["password"]
        user = User.query.filter_by(idapp=int(idapp)).first()
        if not user or not check_password_hash(user.password, password):
            flash('Your id or password is wrong.Please recheck','error')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            return redirect(url_for('main.profile',id=idapp))

    return render_template('login.html')
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    pass
