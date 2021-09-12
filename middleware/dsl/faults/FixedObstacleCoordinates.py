import random
from dsl.mission.Message import Message

class FixedObstacleCoordinates:

    coors = []
    def __init__(self, obstacle_id, x, y, z):
        self.obstacle_id = obstacle_id
        self.x = x
        self.y = y
        self.z = z
        self.message = Message("mFixedObstacleCoordinates", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission):
        o = mission.obstacles[self.obstacle_id]
        o.area.center.x = self.x
        o.area.center.y = self.y
        o.area.center.z = self.z
    
    def mutate(self):
        self.x = random.randint(-1000, 1000)
        self.y = random.randint(-1000, 1000)
        self.z = 1