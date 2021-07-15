class GoalDependencies:
	dependencies = []
	earliestStartTime = 0.0
	latestFinishTime = 0.0
	
	def __init__(self, earliestStartTime, latestFinishTime):
		self.earliestStartTime = earliestStartTime
		self.latestFinishTime = latestFinishTime
	
	def addDependency(self, dependency):
		self.dependencies.add(dependency)

	def isReady(self, timeNow):
		depsReady = True	
		for goal in self.dependencies:
			if not goal.isReady(timeNow):
				depsReady = False
		return depsReady and (timeNow >= self.earliestStartTime) and (timeNow <= self.latestFinishTime)

	def isLate(self, timeNow):
		return timeNow > self.latestFinishTime

	def getDependencies(self):
		return self.dependencies