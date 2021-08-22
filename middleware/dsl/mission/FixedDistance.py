from math import dist
from .GoalTask import GoalTask

class FixedDistance(GoalTask):
    
    def __init__(self, d):
        self.distance = d
