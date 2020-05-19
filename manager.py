from flask_script import Manager, Server
from flask_script import Manager
from app import create_app
from flask_migrate import  MigrateCommand

app = create_app()
manager=Manager(app)
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.add_command("runserver", Server(use_debugger=True,host='0.0.0.0', port=8000))
    manager.run()
    #python manager.py runserver -h 0.0.0.0 -p 8000
