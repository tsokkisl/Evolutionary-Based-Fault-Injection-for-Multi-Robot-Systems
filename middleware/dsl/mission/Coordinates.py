import math

class Coordinates:
		
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y
	
	def get_z(self):
		return self.z
	
	def distance_sqr(self, c):
		return math.pow((c.x - self.x),2.0) + math.pow((c.y - self.y), 2.0)
	
	def distance(self, c):
		return math.sqrt(self.distance_sqr(c))
	
	def find_closest_point(self, coors):
		closest = []
		distance = math.MAX_VALUE
		for c in coors:
			d = self.distance(c)
			if d < distance:
				closest = c
				distance = d
		return closest
	
	def get_coors(self):
		return [int(self.get_x()), int(self.get_y()), int(self.get_z())]