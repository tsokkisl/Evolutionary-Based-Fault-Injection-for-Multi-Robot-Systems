from random import sample
from .SubComponent import SubComponent
from enum import Enum
import random

class Sensor(SubComponent):

	def __init__(self, id, pid, sensor_type, energy_per_sample, samples_per_second):
		self.sensor_type = sensor_type
		self.ID = id
		self.parent_ID = pid
		self.state = "Active"
		self.energy_per_sample = energy_per_sample
		self.samples_per_second = samples_per_second
		self.valid_sample_probability = 1 / samples_per_second
		self.samples = []
		self.last_sample = 0
		self.parent = None

	def set_parent(self, parent):
		self.parent = parent
		
	def get_type(self):
		return self.sensorType
	
	def sensor_type_to_string(self, st):
		return st.name()

	def stop(self):
		self.state = "Inactive"

	def start(self):
		self.state = "Active"

	def register_energy_usage(self):
		energy_required = self.samples_per_second * self.energy_per_sample
		self.parent.deplete_energy(energy_required)

	def generate_samples(self):
		samples = 0
		for _ in range(self.samples_per_second):
			if random.random() <= self.valid_sample_probability:
				samples += 1
		self.register_energy_usage()
		return samples