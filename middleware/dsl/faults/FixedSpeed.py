import random

class FixedSpeed:
    
    def __init__(self, message, speed):
        self.message = message
        self.speed = speed
    
    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.speed = self.speed
        if r.speed < 0: r.speed = 0

    def mutate(self):
        self.speed = random.randint(1, 15)