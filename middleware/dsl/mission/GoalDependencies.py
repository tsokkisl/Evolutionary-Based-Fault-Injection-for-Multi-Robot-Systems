class GoalDependencies:
	
	def __init__(self, depts):
		self.dependencies = []
		self.dependencies = depts

	def add_dependency(self, dependency):
		self.dependencies.add(dependency)

	def is_ready(self, timeNow):
		depsReady = True	
		for goal in self.dependencies:
			if not goal.isReady(timeNow):
				depsReady = False
		return depsReady and (timeNow >= self.earliestStartTime) and (timeNow <= self.latestFinishTime)

	def is_late(self, timeNow):
		return timeNow > self.latestFinishTime

	def get_dependencies(self):
		return self.dependencies