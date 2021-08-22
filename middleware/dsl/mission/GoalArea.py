from .Area import Area;

class GoalArea:

	def __init__(self, a):
		self.area = a
		
	def isDynamic(self):
		return False