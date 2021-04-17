import requests
import logging

from Config import Config
from dtos.EventDTO import EventDTO, SensorType, EventType
from dtos.sensors.DistanceSensorDTO import DistanceSensorDTO, DistanceSensorType
from services.JsonConvert import JsonConvert

logger = logging.getLogger('root')

class EventService:

    def send_distance_sensor_event(self):
        data = JsonConvert.to_json(EventDTO(SensorType.DISTANCE, EventType.TRIGGERED, DistanceSensorDTO(DistanceSensorType.value)))
        logger.info(f"Sending event distance sensor event {data}")
        requests.post(f'{Config.externalServerUrl}/events/distance',
                      headers={'API-Key': Config.apiKey, 'Content-type': 'application/json', 'Accept': 'application/json'},
                      data=data)