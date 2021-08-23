from dsl.mission.Message import Message

class ActivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor
        self.message = Message("mActivateSensor", "gid", "name", "sender", "receiver", "data")

    def run(self, mission):
        self.sensor.start()