import random

class FixedSampleRate:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
        s = mission.robots[self.message.get_from().ID].subcomponents[self.message.get_from().ID]
        s.samples_per_second = self.val