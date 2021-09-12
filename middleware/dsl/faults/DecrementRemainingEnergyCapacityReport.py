import random

class DecrementRemainingEnergyCapacityReport:

    def __init__(self, message, val):
        self.message = message
        self.val = val

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy -= r.current_energy * (self.val / 100)

    def mutate(self):
        self.val = random.randint(10, 20)