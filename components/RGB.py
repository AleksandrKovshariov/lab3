from gpiozero import PWMLED


class RGB:
    __red: PWMLED
    __green: PWMLED
    __blue: PWMLED
    __running: PWMLED or None = None

    def __init__(self, red: int, green: int, blue: int):
        self.__red = PWMLED(red)
        self.__green = PWMLED(green)
        self.__blue = PWMLED(blue)

    def turn_off(self):
        self.__red.value = 0
        self.__green.value = 0
        self.__blue.value = 0
        self.__running = None

    def run(self, led: PWMLED):
        if not self.__running == led:
            self.turn_off()
            led.value = 1
            self.__running = led

    def red(self):
        self.run(self.__red)

    def green(self):
        self.run(self.__green)

    def blue(self):
        self.run(self.__blue)
