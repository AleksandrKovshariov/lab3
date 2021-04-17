from typing import TypeVar, Generic

T = TypeVar('T')


class EventDTO(Generic[T]):
    def __init__(self, sensorType: str, eventType: str, sensorData: T):
        self.sensorType = sensorType
        self.eventType = eventType
        self.sensorData = sensorData
