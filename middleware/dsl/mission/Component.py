from .IntProperty import IntProperty
from .StringProperty import StringProperty
from .DoubleProperty import DoubleProperty
from .CoordinateProperty import CoordinateProperty

class Component:

	def __init__(self):
		self.intProperties = {}
		self.stringProperties = {}
		self.doubleProperties = {}
		self.coordinateProperties = {}
	
	def set_int_component_property(self, name, value):
		self.intProperties[name] = IntProperty(name, value)
	
	def set_parent(self, parent):
		self.parent = parent
	
	def set_double_component_property(self, name, value):
		self.doubleProperties[name] =  DoubleProperty(name, value)
	
	def set_string_component_property(self, name, value):
		self.stringProperties[name] =  StringProperty(name,value)
	
	def set_coordinate_component_property(self, name, value):
		self.coordinateProperties[name] =  CoordinateProperty(name, value)

	def get_int_component_property(self, name):
		p = self.intProperties[name]
		if p != None:
			return p.getValue()
		return None
	
	def get_string_component_property(self, name):
		p = self.stringProperties[name]
		if p != None:
			return p.getValue()
		return None
	
	def get_double_component_property(self, name):
		p = self.doubleProperties[name]
		if p != None:
			return p.getValue()
		return None
	
	def get_coordinate_component_property(self, name):
		p = self.coordinateProperties[name]
		if p != None:
			return p.getValue()
		return None

	def get_parent(self):
		return self.parent
