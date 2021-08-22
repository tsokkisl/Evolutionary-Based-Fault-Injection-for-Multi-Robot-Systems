class Server:
	
	def __init__(self, id, name):
		self.sub_components = []
		self.name = name
		self.ID = id

	def getName(self):
		return self.name
