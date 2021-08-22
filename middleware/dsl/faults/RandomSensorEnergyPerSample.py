class RandomSensorEnergyPerSample:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def run(self, mission):
        s = mission.robots[self.message.get_from().parent_ID].subcomponents[self.message.get_from().ID]
        s.energy_per_sample = self.val