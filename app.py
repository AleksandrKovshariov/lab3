from flask import Flask, jsonify
from flask_script import Manager
from FlaskServer import FlaskServer
from components.RGB import RGB
from services.ComponentService import ComponentService

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())


@app.route('/rgb', methods=['PUT'])
def rbg():
    ComponentService().unlock_number()
    return jsonify(
        {'status': 'acknowledged'}
    )


if __name__ == '__main__':
    manager.run()
