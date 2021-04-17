import importlib.util
import logging

from components.sensors.DistanceSensor import DistanceSensor

logger = logging.getLogger('root')

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    logger.error("Using FAKE RPi")
    import FakeRPi.GPIO as GPIO


class ComponentService:
    left_distance_sensor = DistanceSensor(21)
    right_distance_sensor = DistanceSensor(25)