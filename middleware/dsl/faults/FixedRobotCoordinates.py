class FixedRobotCoordinates:

    coors = []
    def __init__(self, message, x, y, z):
        self.message = message
        self.coors.append(x)
        self.coors.append(y)
        self.coors.append(z)

    def exec_fault(self, mission):
        r = mission.robots[self.message.get_from().ID]
        r.position.x = self.coors[0]
        r.position.y = self.coors[1]
        r.position.z = self.coors[2]