from .SubComponent import SubComponent

class MotionSource(SubComponent):
	energyPerDistance = 0
	
	def __init__(self, energyPerDistance):
		self.energyPerDistance = energyPerDistance
	
	def getEnergyPerDistance(self):
		return self.energyPerDistance
