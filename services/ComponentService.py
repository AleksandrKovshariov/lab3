import logging

from components.sensors.DistanceSensor import DistanceSensor

logger = logging.getLogger('root')

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()


class ComponentService:
    left_distance_sensor = DistanceSensor(21)
    right_distance_sensor = DistanceSensor(25)