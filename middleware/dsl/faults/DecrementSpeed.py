class DecrementSpeed:
    
    def __init__(self, message, val):
        self.message = message
        self.val = val
    
    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.speed -= self.val
        if r.speed < 0: r.speed = 0
