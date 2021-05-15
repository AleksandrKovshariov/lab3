from flask import Flask
from flask_script import Manager

from FlaskServer import FlaskServer
from services.ComponentService import ComponentService

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())

@app.route('/')
def hello_world():
    ComponentService().lock_door()
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
