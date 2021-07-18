class Server:
	sub_components = []
	
	def __init__(self, id, name):
		self.name = name
		self.ID = id

	def getName(self):
		return self.name
