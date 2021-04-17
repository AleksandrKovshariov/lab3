from typing import TypeVar, Generic
import json

T = TypeVar('T')


class EventDTO(Generic[T]):
    def __init__(self, sensorType: str, eventType: str, sensorData: T):
        self.sensorType = sensorType
        self.eventType = eventType
        self.sensorData = sensorData

    def to_json(self):
        return json.dumps(self, default=lambda o: o._asdict)
