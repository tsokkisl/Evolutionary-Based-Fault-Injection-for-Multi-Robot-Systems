from .CProperty import CProperty

class StringProperty(CProperty):
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def getValue(self):
		return self.value