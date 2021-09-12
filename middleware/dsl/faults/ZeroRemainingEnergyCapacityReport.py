class ZeroRemainingEnergyCapacityReport:

    def __init__(self, message, capacity):
        self.message = message
        self.capacity = capacity

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy = self.capacity

    def mutate(self):
        self.capacity = 0