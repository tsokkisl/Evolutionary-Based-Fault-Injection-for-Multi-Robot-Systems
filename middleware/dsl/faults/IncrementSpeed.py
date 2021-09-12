import random

class IncrementSpeed:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.speed += self.val

    def mutate(self):
        self.val = random.randint(1, 10)
