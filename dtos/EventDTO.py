from typing import TypeVar, Generic
from enum import Enum

T = TypeVar('T')


class SensorType(Enum):
    DISTANCE = 'DISTANCE'


class EventDTO(Generic[T]):
    def __init__(self, sensorType: SensorType, sensorData: T):
        self.sensorType: str = sensorType.value
        self.sensorData = sensorData
