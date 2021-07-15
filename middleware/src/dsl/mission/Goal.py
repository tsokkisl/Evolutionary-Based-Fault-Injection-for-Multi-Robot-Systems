from enum import Enum

class Goal:

	results = []

	class GoalStatus(Enum):
		PENDING = 1,
		STARTED = 2,
		COMPLETED = 3,
		VIOLATED = 4,
		MISSED = 5
	
	status = GoalStatus.PENDING
	
	def __init__(self, name, mission, dependencies, members, goalArea, goalTask, messages):
		self.name = name
		self.mission= mission
		self.dependencies = dependencies
		self.members = members
		self.goalArea = goalArea
		self.goalTask = goalTask
		self.messages = messages

	def __init__(self, name, mission, dependencies, members, goalTask, messages):
		self.name = name
		self.mission= mission
		self.dependencies = dependencies
		self.members = members
		self.goalTask = goalTask
		self.messages = messages

	def getStatus(self):
		return self.status
	
	def getName(self):
		return self.name
	
	def setStatus(self, gs):
		self.status = gs

	def isReady(self, time):
		self.dependencies.isReady(time)

	def isLate(self, time):
		self.dependencies.isLate(time)

	def test(self):
		self.action.test(self.mission, self.members)
	
	def getGoalArea(self):
		return self.goalArea

	def setGoalResult(self, goal_result):
		self.results.add(goal_result)

	def getGoalResults(self):
		return self.results

	def setDependency(self, dependency):
		if self != dependency:
			self.dependencies.addDependency(dependency)

	def allDependenciesCompleted(self):
		for dep in self.dependencies.getDependencies():
			if not dep.status == self.GoalStatus.COMPLETED:
				return False
		return True