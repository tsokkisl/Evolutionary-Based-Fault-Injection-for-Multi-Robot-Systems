from .EnergyResource import EnergyResource

class Battery(EnergyResource):
	totalEnergy = 0
	currentEnergy = 0
	
	def __init__(self, energy):
		self.totalEnergy = energy
	
	def getTotalEnergy(self):
		return self.totalEnergy
	
	def isEnergyDeplenished(self):
		return self.currentEnergy == 0
	
	def spendEnergy(self, e):
		self.currentEnergy -= e
		if self.currentEnergy < 0:
			currentEnergy = 0

	def getRemainingEnergyPercentage(self):
		return (self.currentEnergy) / (self.totalEnergy)