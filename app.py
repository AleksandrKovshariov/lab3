from flask import Flask, jsonify, send_from_directory
from flask_script import Manager
from FlaskServer import FlaskServer
from services.ComponentService import ComponentService

app = Flask(__name__)
manager = Manager(app)

manager.add_command('runserver', FlaskServer())


@app.route('/rgb', methods=['PUT'])
def rbg():
    ComponentService().blink()
    return jsonify(
        {'status': 'acknowledged'}
    )

@app.route('/morse', methods=['PUT'])
def morse():
    ComponentService().morse()
    return jsonify(
        {'status': 'acknowledged'}
    )


@app.route('/data', methods=['GET'])
def data():
    data_val = ComponentService().data()
    return jsonify(
        {'data': data_val}
    )


@app.route('/')
def html():
    return send_from_directory('html', 'index.html')


if __name__ == '__main__':
    manager.run()
