class Obstacle:
	
	def __init__(self, id, area):
		self.area = area
		self.ID = id		
	
	def getLabel(self):
		return self.label
	
	def getCoordinates(self):
		return self.polygon