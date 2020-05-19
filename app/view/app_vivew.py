from flask import Blueprint
from flask import render_template
from app.model import db
from app.model.user_model import MyUser
vive=Blueprint('second',__name__)

@vive.route("/")
def hello_world():
    return 'hello Flask'


@vive.route("/create_database")
def create_data():
    db.create_all()
    return "sqlite create database  OK"

@vive.route("/add_data")
def add_data():
    u1=MyUser(username="Linux",password='198641')
    db.session.add(u1)
    db.session.commit()
    return "sqlite add  data  OK"

@vive.route("/delete_database")
def delete_data():
    db.drop_all()
    return "sqlite delete database  OK"

@vive.route("/indexl")
def indel():
    return render_template("index.html")