class FixedSpeed:
    
    def __init__(self, message, speed):
        self.message = message
        self.speed = speed
    
    def run(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.speed = self.speed
