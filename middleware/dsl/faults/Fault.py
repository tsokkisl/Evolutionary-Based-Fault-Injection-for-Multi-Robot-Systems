from dsl.faults.ActivateSensor import ActivateSensor
from dsl.faults.DeactivateSensor import DeactivateSensor
from dsl.faults.StartRobot import StartRobot
from dsl.faults.StopRobot import StopRobot

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

	def exec_fault(self, currentTime, mission, mrs):
		if currentTime >= self.start and currentTime <= self.finish:
			if isinstance(self.ft, ActivateSensor) or isinstance(self.ft, DeactivateSensor) or isinstance(self.ft, StartRobot) or isinstance(self.ft, StopRobot):
				self.ft.exec_fault(mission, mrs)
			else: self.ft.exec_fault(mission)