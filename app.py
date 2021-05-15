from flask import Flask, jsonify
from flask_script import Manager

from FlaskServer import FlaskServer
from services.ComponentService import ComponentService

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())


@app.route('/number/lock', methods=['PUT'])
def lock_number():
    ComponentService().lock_number()
    return jsonify(
        {'status': 'acknowledged'}
    )


@app.route('/number/unlock', methods=['PUT'])
def unlock_number():
    ComponentService().unlock_number()
    return jsonify(
        {'status': 'acknowledged'}
    )


if __name__ == '__main__':
    manager.run()
