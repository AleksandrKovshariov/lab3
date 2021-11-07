from flask import Flask, jsonify
from flask_script import Manager
from FlaskServer import FlaskServer
from components.RGB import RGB

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())


@app.route('/rgb', methods=['PUT'])
def rbg():
    rgb = RGB(19, 13, 26)
    rgb.red()
    return jsonify(
        {'status': 'acknowledged'}
    )


if __name__ == '__main__':
    manager.run()
