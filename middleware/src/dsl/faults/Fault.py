class Fault:
	name = ""
	startTime = 0.0
	finishTime = 0.0
	
	def __init__(self, name, ft, earliestStartTime, latestFinishTime, probability):
		self.name = name
		self.type = ft
		self.startTime = earliestStartTime
		self.finishTime = latestFinishTime
		self.probability = probability

	def getName(self):
		return self.name
	
	def getEarliestStartTime(self):
		return self.startTime
	
	def getLatestEndTime(self):
		return self.finishTime