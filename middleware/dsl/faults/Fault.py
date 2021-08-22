class Fault:
	name = ""
	start = 0.0
	finish = 0.0
	
	def __init__(self, ft, start, finish):
		self.ft = ft
		self.start = start
		self.finish = finish

	def getName(self):
		return self.name
	
	def getEarlieststart(self):
		return self.start
	
	def getLatestEndTime(self):
		return self.finish

	def exec_fault(self, currentTime, mission):
		if currentTime >= self.start and currentTime <= self.finish:
			self.ft.exec_fault(mission)