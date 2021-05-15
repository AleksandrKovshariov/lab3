from flask import Flask
from flask_script import Manager

from FlaskServer import FlaskServer
from services.ComponentService import ComponentService

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())


@app.route('/number/lock')
def lock_number():
    ComponentService().lock_number()
    return "Ok"


@app.route('/number/unlock')
def unlock_number():
    ComponentService().unlock_number()
    return "Ok"


if __name__ == '__main__':
    manager.run()
