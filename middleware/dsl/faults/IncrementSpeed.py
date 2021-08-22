class IncrementSpeed:
    
    def __init__(self, message, percentage):
        self.message = message
        self.percentage = percentage
    
    def run(self, mission):
        r = mission.robots[self.message.get_from().ID]
        current_speed = r.speed
        r.speed = current_speed + current_speed * self.percentage
