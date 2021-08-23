class ZeroSpeed:
    
    def __init__(self, message, speed):
        self.message = message
        self.speed = speed
    
    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.speed = self.speed
