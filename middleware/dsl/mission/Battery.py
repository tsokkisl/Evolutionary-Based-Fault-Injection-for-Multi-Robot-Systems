from .EnergyResource import EnergyResource

class Battery(EnergyResource):
	total_energy = 0
	current_energy = 0
	
	def __init__(self, id, energy):
		self.ID = id
		self.total_energy = energy
	
	def get_total_energy(self):
		return self.total_energy
	
	def is_energy_deplenished(self):
		return self.current_energy == 0
	
	def spend_energy(self, e):
		self.current_energy -= e
		if self.current_energy < 0:
			self.current_energy = 0

	def get_remaining_energy_percentage(self):
		return (self.current_energy) / (self.total_energy)