import random

class IncrementRemainingEnergyCapacityReport:

    def __init__(self, message, percentage):
        self.message = message
        self.percentage = percentage

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy += r.current_energy * (self.percentage / 100)

    def mutate(self):
        self.percentage = random.randint(5, 10)