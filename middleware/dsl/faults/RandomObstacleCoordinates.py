from dsl.mission.Message import Message
import random

class RandomObstacleCoordinates:

    def __init__(self, obstacle_id, x, y, z):
        self.obstacle_id = obstacle_id
        self.x = x
        self.y = y
        self.z = z
        self.message = Message("mRandomObstacleCoordinates", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission):
        o = mission.obstacles[self.obstacle_id]
        o.area.center.x = self.x
        o.area.center.y = self.y
        o.area.center.z = self.z
    
    def mutate(self):
        self.x = random.randint(-2500, 2500)
        self.y = random.randint(-2500, 2500)
        self.z = 1