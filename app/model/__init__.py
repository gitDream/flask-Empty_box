from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

def init_model(app):
    db.init_app(app)
    return db
