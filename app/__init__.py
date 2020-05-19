from flask import Flask
from app.view import init_view
from app.model import init_model
from flask_migrate import Migrate
from app.model import db as model
#from app import setting

#mysql config
def setting_app(app):
    app.config.from_pyfile("./setting.py")
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config['MODIFICATIONS']

#数据迁移
def setting_migrate(app,db):
    migrate=Migrate()
    migrate.init_app(app,db)

#MVC 初始化
def create_app():
    app = Flask(__name__)
    setting_app(app)
    init_model(app)
    init_view(app)
    setting_migrate(app,model)
    return app