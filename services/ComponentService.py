import logging
from time import sleep

from components.sensors.DistanceSensor import DistanceSensor
from components.RGB import RGB

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils

    fake_rpigpio.utils.install()

logger = logging.getLogger('root')


class ComponentService(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(ComponentService, self).__new__(self)
            self.left_distance_sensor = DistanceSensor(21)
            self.right_distance_sensor = DistanceSensor(25)
            self.rgb = RGB(19, 13, 26)
        return self._instance

    def blink(self):
        logger.info(f"Blinking")
        self.rgb.red()
        sleep(1000)
        self.rgb.blue()
        sleep(1000)
        self.rgb.blue()
        sleep(1000)