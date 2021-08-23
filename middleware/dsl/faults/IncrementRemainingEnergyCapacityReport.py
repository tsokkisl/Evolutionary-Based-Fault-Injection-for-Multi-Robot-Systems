class IncrementRemainingEnergyCapacityReport:

    def __init__(self, message, val):
        self.message = message
        self.val = val

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.current_energy += self.val