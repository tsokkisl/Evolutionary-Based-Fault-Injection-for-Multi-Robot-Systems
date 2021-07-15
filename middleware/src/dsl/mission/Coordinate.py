import math

class Coordinate:
	x = 0
	y = 0
	z = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getZ(self):
		return self.z
	
	def distanceSqr(self, c):
		return math.pow((c.x - self.x),2.0) + math.pow((c.y - self.y), 2.0)
	
	def distance(self, c):
		return math.sqrt(self.distanceSqr(c))
	
	def findClosestPoint(self, coors):
		closest = []
		distance = math.MAX_VALUE
		for c in coors:
			d = self.distance(c)
			if d < distance:
				closest = c
				distance = d
		return closest