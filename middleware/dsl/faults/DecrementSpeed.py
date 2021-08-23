class DecrementSpeed:
    
    def __init__(self, message, percentage):
        self.message = message
        self.percentage = percentage
    
    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        current_speed = r.get_double_component_property("SPEED")
        r.set_double_component_property("SPEED", current_speed - current_speed * self.percentage)
