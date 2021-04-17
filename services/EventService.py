import requests

from FlaskServer import Config
from dtos.EventDTO import EventDTO
from dtos.sensors.DistanceSensorDTO import DistanceSensorDTO


class EventService:

    def sendDistanceSensorEvent(self):
        data = EventDTO[DistanceSensorDTO]('DISTANCE', 'TRIGGERED', DistanceSensorDTO('LEFT')).to_json()
        requests.post(f'{Config.externalServerUrl}/events/distance',
                      headers={'API-Key': Config.apiKey},
                      data=data)