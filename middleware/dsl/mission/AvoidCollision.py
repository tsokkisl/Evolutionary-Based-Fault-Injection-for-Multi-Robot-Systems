from .GoalTask import GoalTask

class AvoidCollision(GoalTask):
	
	def __init__(self, robots, obstacles):
		self.robots = robots
		self.obstacles = obstacles