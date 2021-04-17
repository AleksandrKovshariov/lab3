from typing import TypeVar, Generic
from enum import Enum

T = TypeVar('T')


class SensorType(Enum):
    DISTANCE = 'DISTANCE'


class EventType(Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'
    TRIGGERED = 'TRIGGERED'


class EventDTO(Generic[T]):
    def __init__(self, sensorType: SensorType, eventType: EventType, sensorData: T):
        self.sensorType: str = sensorType.value
        self.eventType: str = eventType.value
        self.sensorData = sensorData
