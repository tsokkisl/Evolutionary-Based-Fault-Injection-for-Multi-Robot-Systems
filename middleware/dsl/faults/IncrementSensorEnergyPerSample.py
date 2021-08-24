from dsl.mission.Sensor import Sensor

class IncrementSensorEnergyPerSample:
    
    def __init__(self, message, percentage):
        self.message = message
        self.percentage = percentage
    
    def exec_fault(self, mission):
        robot = mission.robots[self.message.get_from().ID]
        for sc in robot.subcomponents.values():
            if isinstance(sc, Sensor):
                sc.energy_per_sample += sc.energy_per_sample * (self.percentage / 100)
