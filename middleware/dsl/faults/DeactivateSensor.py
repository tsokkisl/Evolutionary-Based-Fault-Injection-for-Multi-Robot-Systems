from dsl.mission.Message import Message

class DeactivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor
        self.message = Message("mDeactivateSensor", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission):
        self.sensor.stop()