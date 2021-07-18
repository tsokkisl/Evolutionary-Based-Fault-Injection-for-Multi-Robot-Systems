from .SubComponent import SubComponent
from enum import Enum

class Sensor(SubComponent):
	
	class SensorType(Enum):
		SONAR = 1,
		GPS_POSITION = 2,
		CAMERA = 3
	
	def __init__(self, id, sensor_type):
		self.sensorType = self.SensorType.sensor_type
		self.ID = id

	def getType(self):
		return self.sensorType
	
	def sensorTypeToString(self, st):
		return st.name()