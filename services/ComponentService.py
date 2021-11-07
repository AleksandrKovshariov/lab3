import logging
from time import sleep

from components.sensors.Hall import Hall
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
            self.hall = Hall(pin=21)
            self.rgb = RGB(19, 13, 26)
        return self._instance

    def blink(self):
        logger.info(f"Blinking")
        self.rgb.red()
        sleep(1.5)
        self.rgb.green()
        sleep(1.5)
        self.rgb.blue()
        sleep(1.5)
        self.rgb.turn_off()

    def data(self):
        logging.info("Get hall sensor data")
        val = self.hall.value
        logger.info(f"Hall sensor data {val}")
        return val



