import json


class DistanceSensorDTO:
    def __init__(self, distanceSensor: str):
        self.distanceSensor = distanceSensor

    def to_json(self):
        return json.dumps(self, default=lambda o: self.__dict__)
