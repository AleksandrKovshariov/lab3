import requests
import logging

from Config import Config
from dtos.EventDTO import EventDTO, SensorType, EventType
from dtos.sensors.DistanceSensorDTO import DistanceSensorDTO, DistanceSensorType
from services.JsonConvert import JsonConvert

logger = logging.getLogger('root')

class EventService:

    @staticmethod
    def send_distance_sensor_event(sensor_type: DistanceSensorType):
        data = JsonConvert.to_json(EventDTO(EventType.TRIGGERED, SensorType.DISTANCE, DistanceSensorDTO(sensor_type)))
        logger.info(f"Sending event: distance sensor event {data}")
        requests.post(f'{Config.externalServerUrl}/events/distance',
                      headers={'API-Key': Config.apiKey, 'Content-type': 'application/json'},
                      data=data)