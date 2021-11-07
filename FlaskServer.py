
from flask_script import Server
from log import setup_logger

setup_logger('root')


class FlaskServer(Server):
    def __call__(self, app, *args, **kwargs):
        return Server.__call__(self, app, *args, **kwargs)
