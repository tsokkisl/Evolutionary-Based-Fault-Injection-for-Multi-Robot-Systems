from .SubComponent import SubComponent

class MotionSource(SubComponent):
	energy_per_distance_unit = 0
	
	def __init__(self, id, energy_per_distance_unit):
		self.ID = id
		self.energy_per_distance_unit = energy_per_distance_unit
	
	def get_energy_per_distance_unit(self, robot_speed):
		return self.energy_per_distance_unit * robot_speed
