from .SubComponent import SubComponent
from enum import Enum

class Sensor(SubComponent):
	
	class SensorType(Enum):
		SONAR = 1,
		GPS_POSITION = 2,
		CAMERA = 3

	def __init__(self, t):
		self.sensorType = self.SensorType.t
	
	def __init__(self, sensor_type):
		self.sensorType = sensor_type
	
	def getType(self):
		return self.sensorType
	
	def sensorTypeToString(self, st):
		return st.name()