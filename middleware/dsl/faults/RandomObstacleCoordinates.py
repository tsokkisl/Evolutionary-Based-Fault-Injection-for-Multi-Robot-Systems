class RandomObstacleCoordinates:

    coors = []
    def __init__(self, obstacle_id, x, y, z):
        self.obstacle_id = obstacle_id
        self.coors.append(x)
        self.coors.append(y)
        self.coors.append(z)

    def run(self, mission):
        o = mission.ostacles[self.obstacle_id]
        o.area.center.x = self.coors[0]
        o.area.center.y = self.coors[1]
        o.area.center.z = self.coors[2]