from flask import Blueprint, render_template, redirect, url_for, request,jsonify,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from coronatracer.extensions import db
from coronatracer.models import User
from coronatracer.script1 import Graph
import sqlite3

main = Blueprint('main',__name__)
@main.route('/')
def index():
    return render_template('index3.html')

@main.route('/service-worker.js')
def sw():
    return main.send_static_file('service-worker.js')

@main.route('/profile/<id>',methods=["POST","GET"])
@login_required
def profile(id):
    session['var']=id
    person=User.query.filter_by(idapp=id).first()
    if person.color=="R":
        return render_template('profiler.html',name=person.name)
    elif person.color=="G":
        return render_template('profileg.html',name=person.name)
    elif person.color=="O":
        return render_template('profileo.html',name=person.name)
@main.route('/profile/add/',methods=["POST","GET"])
@login_required
def add():
    return render_template('add.html')
@main.route('/convert',methods=["POST","GET"])
def convert():
    contact1=request.form.get("contact1")
    contact2=request.form.get("contact2")
    if contact1!=session['var']:
        return jsonify({"success":False})
    person2=User.query.filter_by(idapp=int(contact2)).first()
    person=User.query.filter_by(idapp=int(contact1)).first()
    if(person.color!="G" or person2.color!="G" or person2==None):
        return jsonify({"success":False})
    if contact2 not in person.contacts:
        k=person.contacts+str(contact2)+" "
        person.contacts=k
        j=person.time+'0'+' '
        person.time=j
        person2=User.query.filter_by(idapp=int(contact2)).first()
        a=person2.contacts+str(contact1)+" "
        person2.contacts=a
        t=person2.time+'0'+' '
        person2.time=t
        db.session.commit()
        return jsonify({"success": True, "id": contact2})

@main.route('/profile/update',methods=["POST","GET"])
@login_required
def update():
    if request.method=="POST":
        color=request.form["btn"]
        id=request.form["id1"]
        k=session['var']
        if id!=k:
            flash('Use your own id','error')
            return redirect(url_for('main.update'))
        if color=="G":
            person=User.query.filter_by(idapp=int(id)).first()
            if person.color=="O":
                person.color="G"
                db.session.commit()
            flash('Your response is recorded','info')
            return redirect(url_for('main.profile',id=id))
        elif color=="R":
            edges=[]
            user={}
            color={}
            users=User.query.all()
            for user in users:
                for k in user.contacts.split(" "):
                    if k!='':
                        edges.append((user.idapp,int(k)))
            print(edges)
            g=Graph(edges)
            no,orange=g.bfsq(int(id))
            print(orange)
            for i in orange:
                for user in users:
                    person=User.query.filter_by(idapp=int(i)).first()
                    contacts=user.contacts.rstrip().split(" ")
                    time=user.time.rstrip().split(" ")
                    if (str(i) in contacts and time[contacts.index(str(i))]!=' ' and int(time[contacts.index(str(i))])<=14 and person.color!='R'):
                        person.color="O"
                        print(person.idapp)
            user=User.query.filter_by(idapp=int(id)).first()
            user.color="R"
            print(user.idapp)

        else:
            edges=[]
            user={}
            color={}
            users=User.query.all()
            for user in users:
                for k in user.contacts.split(" "):
                    if k!='':
                        edges.append((user.idapp,int(k)))
            print(edges)
            g=Graph(edges)
            no,orange=g.bfsq(int(id))
            print(orange)
            for i in orange:
                for user in users:
                    person=User.query.filter_by(idapp=int(i)).first()
                    contacts=user.contacts.rstrip().split(" ")
                    time=user.time.rstrip().split(" ")
                    if (str(i) in contacts and time[contacts.index(str(i))]!=' ' and int(time[contacts.index(str(i))])<=14 and person.color!='R'):
                        person.color="O"
                        print(person.idapp)
            user=User.query.filter_by(idapp=int(id)).first()
            user.color="O"
            print(user.idapp)

        db.session.commit()
        flash('Your response is recorded','info')
        return redirect(url_for('main.profile',id=id))

    return render_template('update.html')

@main.route('/logout',methods=["POST","GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@main.route('/updatetime',methods=["POST","GET"])
@login_required
def updatetime():
    users=User.query.all()
    for user in users:
        k=''
        for j in user.time.rstrip().split(" "):
            string=str(int(j)+1)
            k=k+string+' '
        user.time=k
        db.session.commit()
    return redirect(url_for('main.logout'))
@main.route('/reset',methods=["POST","GET"])
@login_required
def reset():
    users=User.query.all()
    for user in users:
        user.color="G"
        user.contacts=''
        user.time=''
        db.session.commit()
    return redirect(url_for('main.index'))
