from functools import partial

from Config import Config
from dtos.sensors.DistanceSensorDTO import DistanceSensorType
from services.ComponentService import ComponentService
from services.EventService import EventService
from flask_script import Server
from log import setup_logger
import requests

setup_logger('root')


class FlaskServer(Server):
    def __call__(self, app, *args, **kwargs):
        self.init()
        return Server.__call__(self, app, *args, **kwargs)

    @staticmethod
    def register_listeners():
        ComponentService().left_distance_sensor.triggered = partial(EventService.send_distance_sensor_event,
                                                                    DistanceSensorType.LEFT)
        ComponentService().right_distance_sensor.triggered = partial(EventService.send_distance_sensor_event,
                                                                     DistanceSensorType.RIGHT)
