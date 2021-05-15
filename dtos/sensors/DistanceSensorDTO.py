from enum import Enum

from dtos.sensors.EventType import EventType


class DistanceSensorType(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


class DistanceSensorDTO:
    def __init__(self, eventType: EventType, distanceSensor: DistanceSensorType):
        self.distanceSensor: str = distanceSensor.value
        self.eventType: str = eventType.value
