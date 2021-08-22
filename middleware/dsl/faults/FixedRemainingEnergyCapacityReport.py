class FixedRemainingEnergyCapacityReport:

    def __init__(self, message, capacity):
        self.message = message
        self.capacity = capacity

    def run(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy = self.capacity