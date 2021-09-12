from dsl.mission.Message import Message

class DeactivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor
        self.message = Message("mDeactivateSensor", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission, mrs):
        mission.robots[self.sensor.parent_ID].subcomponents[self.sensor.ID].stop()
        mrs.robots[self.sensor.parent_ID].subcomponents[self.sensor.ID].stop()

    def mutate(self):
        pass