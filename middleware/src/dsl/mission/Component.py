from middleware.src.dsl.mission.SubComponent import SubComponent
from .Coordinate import Coordinate
from .IntProperty import IntProperty
from .StringProperty import StringProperty
from .DoubleProperty import DoubleProperty
from .CoordinateProperty import CoordinateProperty

class Component:
	intProperties = {}
	stringProperties = {}
	doubleProperties = {}
	coordinateProperties = {}
	
	def setIntComponentProperty(self, name, value):
		self.intProperties.put(name, IntProperty(name, value))
	
	def setParent(self, parent):
		self.parent = parent
	
	def setDoubleComponentProperty(self, name, value):
		self.doubleProperties.put(name, DoubleProperty(name, value))
	
	def setStringComponentProperty(self, name, value):
		self.stringProperties.put(name, StringProperty(name,value))
	
	def setCoordinateComponentProperty(self, name, value):
		self.coordinateProperties.put(name, CoordinateProperty(name,value))

	def getIntComponentProperty(self, name):
		p = self.intProperties.get(name)
		if p != None:
			return p.getValue()
		return None
	
	def getStringComponentProperty(self, name):
		p = self.stringProperties.get(name)
		if p != None:
			return p.getValue()
		return None
	
	def getDoubleComponentProperty(self, name):
		p = self.doubleProperties.get(name)
		if p != None:
			return p.getValue()
		return None
	
	def getCoordinateComponentProperty(self, name):
		p = self.coordinateProperties.get(name)
		if p != None:
			return p.getValue()
		return None

	def getParent(self):
		return self.parent
