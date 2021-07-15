from .CProperty import CProperty

class IntProperty(CProperty):
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def getValue(self):
		return self.value