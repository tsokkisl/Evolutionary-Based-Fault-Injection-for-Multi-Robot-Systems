import random

class RandomRobotCoordinates:

    def __init__(self, message, x, y, z):
        self.message = message
        self.x = x
        self.y = y
        self.z = z

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.position.x = self.x
        r.position.y = self.y
        r.position.z = self.z

    def mutate(self):
        self.x = random.randint(-2500, 2500)
        self.y = random.randint(-2500, 2500)
        self.z = 1