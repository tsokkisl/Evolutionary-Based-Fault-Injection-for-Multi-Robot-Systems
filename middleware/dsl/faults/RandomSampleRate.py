import random
from dsl.mission.Sensor import Sensor

class RandomSampleRate:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
        robot = mission.robots[self.message.get_from().ID]
        for sc in robot.subcomponents.values():
            if isinstance(sc, Sensor):
                sc.samples_per_second = self.val
                if sc.samples_per_second < 0: sc.samples_per_second = 0