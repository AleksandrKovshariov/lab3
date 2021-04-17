from gpiozero import DigitalInputDevice, HoldMixin


class DistanceSensor(HoldMixin, DigitalInputDevice):
    def __init__(self, pin=None,
                 pull_up=True,
                 active_state=None,
                 bounce_time=None,
                 hold_time=1,
                 hold_repeat=False,
                 pin_factory=None):
        super(DistanceSensor, self).__init__(pin, pull_up=pull_up, active_state=active_state,
                                             bounce_time=bounce_time, pin_factory=pin_factory)
        self.hold_time = hold_time
        self.hold_repeat = hold_repeat


DistanceSensor.triggered = DistanceSensor.when_deactivated
