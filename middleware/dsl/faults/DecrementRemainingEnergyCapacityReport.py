class DecrementRemainingEnergyCapacityReport:

    def __init__(self, message, val):
        self.message = message
        self.val = val

    def run(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy -= self.val