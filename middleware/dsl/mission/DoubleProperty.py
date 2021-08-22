from .CProperty import CProperty

class DoubleProperty(CProperty):
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def getValue(self):
		return self.value