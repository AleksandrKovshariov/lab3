from enum import Enum


class DistanceSensorType(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class DistanceSensorDTO:
    def __init__(self, distanceSensor: DistanceSensorType):
        self.distanceSensor: str = distanceSensor.value
