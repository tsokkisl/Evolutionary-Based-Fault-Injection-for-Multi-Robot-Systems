class IncrementSensorEnergyPerSample:
    
    def __init__(self, message, percentage):
        self.message = message
        self.percentage = percentage
    
    def exec_fault(self, mission):
        s = mission.robots[self.message.get_from().parent_ID].subcomponents[self.message.get_from().ID]
        s.energy_per_sample += s.energy_per_sample * self.percentage
