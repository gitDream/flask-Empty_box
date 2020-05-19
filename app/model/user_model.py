from app.model import db
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey


class MyUser(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(16))
    password=db.Column(db.String(32))





