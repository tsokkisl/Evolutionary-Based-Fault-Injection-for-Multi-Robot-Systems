from ..faults import *
from ..mission import *

class FaultSpecification:

	faults = []

	def __init__(self, mission):
		self.mission = mission
