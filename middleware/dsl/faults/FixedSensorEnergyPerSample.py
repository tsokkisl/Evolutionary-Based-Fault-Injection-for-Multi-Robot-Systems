from dsl.mission.Sensor import Sensor

class FixedSensorEnergyPerSample:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
       robot = mission.robots[self.message.get_from().ID]
       for sc in robot.subcomponents.values():
            if isinstance(sc, Sensor):
                sc.energy_per_sample = self.val
                if sc.energy_per_sample < 0: sc.energy_per_sample = 0
