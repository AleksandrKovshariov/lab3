from decouple import config


class Config:
    apiKey = config('API_KEY')
    externalServerUrl = config('EVENT_SERVICE_URL')
    roomNumber = config('ROOM_NUMBER')
