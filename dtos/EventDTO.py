from typing import TypeVar, Generic
from enum import Enum

T = TypeVar('T')


class SensorType(Enum):
    DISTANCE = 'DISTANCE'



class EventDTO(Generic[T]):
    def __init__(self, sensorType: SensorType, eventType: str, sensorData: T):
        self.sensorType = sensorType.value
        self.eventType = eventType
        self.sensorData = sensorData
