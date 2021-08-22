from .Coordinates import Coordinates

import math

class Area :
	
	def __init__(self, c, r):
		self.center = c
		self.radius = r
	
	def width(self):
		return math.abs(self.c1.getX() - self.getX())

	def height(self):
		return math.abs(self.c1.getY() - self.c2.getY())
	
	def left(self):
		return math.min(self.c1.getX(), self.c2.getX())
	
	def bottom(self):
		return math.min(self.c1.getY(), self.c2.getY())
	
	def right(self):
		return math.max(self.c1.getX(), self.c2.getX())
	
	def top(self):
		return math.max(self.c1.getY(), self.c2.getY())
	
	def containsCoordinates(self, c):
		x = c.getX()
		y = c.getY()
		return (x > self.left() and x < self.right() and y > self.bottom() and y < self.top())
