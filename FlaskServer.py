from flask_script import Server
from log import setup_logger
import logging
from decouple import config

setup_logger('root')
logger = logging.getLogger('root')


class FlaskServer(Server):
    def __call__(self, app, *args, **kwargs):
        self.init()
        return Server.__call__(self, app, *args, **kwargs)

    def init(self):
        API_KEY = config('API_KEY')
        print(API_KEY)
