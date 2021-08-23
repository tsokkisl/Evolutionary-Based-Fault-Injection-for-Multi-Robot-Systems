class FixedSensorEnergyPerSample:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
        s = mission.robots[self.message.get_from().ID].subcomponents[self.message.get_from().ID]
        s.energy_per_sample = self.val
