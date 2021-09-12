from dsl.mission.Message import Message

class ActivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor
        self.message = Message("mActivateSensor", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission, mrs):
        mission.robots[self.sensor.parent_ID].subcomponents[self.sensor.ID].start()
        mrs.robots[self.sensor.parent_ID].subcomponents[self.sensor.ID].start()
    
    def mutate(self):
        pass