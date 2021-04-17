import requests

from Config import Config
from dtos.EventDTO import EventDTO
from dtos.sensors.DistanceSensorDTO import DistanceSensorDTO
from services.JsonConvert import JsonConvert


class EventService:

    def sendDistanceSensorEvent(self):
        data = JsonConvert.to_json(EventDTO('DISTANCE', 'TRIGGERED', DistanceSensorDTO('LEFT')))
        print(data)
        requests.post(f'{Config.externalServerUrl}/events/distance',
                      headers={'API-Key': Config.apiKey, 'Content-type': 'application/json'},
                      json=data)