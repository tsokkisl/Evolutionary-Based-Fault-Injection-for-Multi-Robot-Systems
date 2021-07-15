class Obstacle:
	polygon = []
	label = ""
	
	def __init__(self, label, polygon):
		self.polygon = polygon
		self.label = label		
	
	def getLabel(self):
		return self.label
	
	def getCoordinates(self):
		return self.polygon