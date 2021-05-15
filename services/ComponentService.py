import logging

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

    def lock_number(self):
        logger.info(f"Locking number")
        self.rgb.red()

    def unlock_number(self):
        logger.info(f"Unlocking number")
        self.rgb.green()
