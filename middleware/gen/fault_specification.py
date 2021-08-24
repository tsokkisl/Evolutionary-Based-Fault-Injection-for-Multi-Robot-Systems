from dsl.faults.DecrementSpeed import DecrementSpeed
from dsl.faults.DeactivateSensor import DeactivateSensor
from dsl.faults.DelayMessage import DelayMessage
from dsl.faults.FixedRobotCoordinates import FixedRobotCoordinates
from dsl.faults.ZeroRemainingEnergyCapacityReport import ZeroRemainingEnergyCapacityReport
from dsl.faults.Fault import Fault
from dsl.faults.RandomSpeed import RandomSpeed
from dsl.faults.BlockMessage import BlockMessage
from dsl.faults.RandomRobotCoordinates import RandomRobotCoordinates
from dsl.faults.RandomSampleRate import RandomSampleRate
from dsl.faults.ActivateSensor import ActivateSensor
from dsl.faults.DecrementRemainingEnergyCapacityReport import DecrementRemainingEnergyCapacityReport
from dsl.faults.FixedObstacleCoordinates import FixedObstacleCoordinates
from dsl.faults.FixedRemainingEnergyCapacityReport import FixedRemainingEnergyCapacityReport
from dsl.faults.DecrementSensorEnergyPerSample import DecrementSensorEnergyPerSample
from dsl.faults.IncrementRemainingEnergyCapacityReport import IncrementRemainingEnergyCapacityReport
from dsl.faults.ZeroSpeed import ZeroSpeed
from dsl.faults.DecrementSampleRate import DecrementSampleRate
from dsl.faults.FixedSampleRate import FixedSampleRate
from dsl.faults.FixedSensorEnergyPerSample import FixedSensorEnergyPerSample
from dsl.faults.FixedSpeed import FixedSpeed
from dsl.faults.RandomSensorEnergyPerSample import RandomSensorEnergyPerSample
from dsl.faults.StartRobot import StartRobot
from dsl.faults.StopRobot import StopRobot
from dsl.faults.IncrementSampleRate import IncrementSampleRate
from dsl.faults.IncrementSensorEnergyPerSample import IncrementSensorEnergyPerSample
from dsl.faults.IncrementSpeed import IncrementSpeed
from dsl.faults.RandomObstacleCoordinates import RandomObstacleCoordinates
from dsl.faults.RandomRemainingEnergyCapacityReport import RandomRemainingEnergyCapacityReport
from dsl.faults.IncrementSampleRate import IncrementSampleRate
from dsl.faults.IncrementSampleRate import IncrementSampleRate
from dsl.faults.Fault import Fault
import random
import numpy as np
import copy

class FaultSpecification:

	faults = []

	def __init__(self, mission):
	
		self.mission = mission
		
		#Fault Specification 
	
		#Initializing Fault: f1
		ft = ActivateSensor(mission.robots["r1"].subcomponents["s2"])
		self.faults.append(ft)
	
		#Initializing Fault: f2
		ft = BlockMessage(mission.goals["g2"].messages["m4"], 5.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f3
		ft = DecrementRemainingEnergyCapacityReport(mission.goals["g3"].messages["m8"], 10.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f4
		ft = DecrementSampleRate(mission.goals["g5"].messages["m11"], 2) 
		self.faults.append(ft)
	
		#Initializing Fault: f5
		ft = DecrementSensorEnergyPerSample(mission.goals["g3"].messages["m9"], 10.0)
		self.faults.append(ft)
	
		#Initializing Fault: f6
		ft = DecrementSpeed(mission.goals["g3"].messages["m7"], 1) 
		self.faults.append(ft)
	
		#Initializing Fault: f7
		ft = DelayMessage(mission.goals["g4"].messages["m10"], 200.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f8
		ft = FixedObstacleCoordinates(random.randint(1, 8), 2, 1, 9) 
		self.faults.append(ft)
	
		#Initializing Fault: f9
		ft = FixedRemainingEnergyCapacityReport(mission.goals["g3"].messages["m8"], 150.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f10
		ft = FixedRobotCoordinates(mission.goals["g1"].messages["m2"], -1, 7, 7) 
		self.faults.append(ft)
	
		#Initializing Fault: f11
		ft = FixedSampleRate(mission.goals["g3"].messages["m8"], 120) 
		self.faults.append(ft)
	
		#Initializing Fault: f12
		ft = FixedSensorEnergyPerSample(mission.goals["g3"].messages["m9"], 10.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f13
		ft = FixedSpeed(mission.goals["g3"].messages["m7"], 50)
		self.faults.append(ft)
	
		#Initializing Fault: f14
		ft = IncrementRemainingEnergyCapacityReport(mission.goals["g3"].messages["m8"], 10.0)
		self.faults.append(ft)
	
		#Initializing Fault: f15
		ft = IncrementSampleRate(mission.goals["g5"].messages["m11"], 25)
		self.faults.append(ft)
	
		#Initializing Fault: f16
		ft = IncrementSensorEnergyPerSample(mission.goals["g3"].messages["m7"], 22.0)
		self.faults.append(ft)
	
		#Initializing Fault: f17
		ft = IncrementSpeed(mission.goals["g3"].messages["m7"], 10) 
		self.faults.append(ft)
	
		#Initializing Fault: f18
		ft = RandomObstacleCoordinates(random.randint(1, 8), random.randint(-mission.mission_area.radius, mission.mission_area.radius), random.randint(-mission.mission_area.radius, mission.mission_area.radius), random.randint(-mission.mission_area.radius, mission.mission_area.radius)) 
		self.faults.append(ft)
	
		#Initializing Fault: f19
		ft = RandomRemainingEnergyCapacityReport(mission.goals["g3"].messages["m8"], random.uniform(255.0, 1000.0)) 
		self.faults.append(ft)
	
		#Initializing Fault: f20
		ft = RandomRobotCoordinates(mission.goals["g1"].messages["m3"], random.randint(-mission.mission_area.radius, mission.mission_area.radius), random.randint(-mission.mission_area.radius, mission.mission_area.radius), random.randint(-mission.mission_area.radius, mission.mission_area.radius)) 
		self.faults.append(ft)
	
		#Initializing Fault: f21
		ft = RandomSampleRate(mission.goals["g4"].messages["m10"], random.randint(1, 50)) 
		self.faults.append(ft)
	
		#Initializing Fault: f22
		ft = RandomSensorEnergyPerSample(mission.goals["g3"].messages["m7"], random.uniform(11.0, 30.0))
		self.faults.append(ft)
	
		#Initializing Fault: f23
		ft = RandomSpeed(mission.goals["g3"].messages["m8"], random.randint(-10, 10)) 
		self.faults.append(ft)
	
		#Initializing Fault: f24
		ft = StartRobot(mission.robots["r3"])
		self.faults.append(ft)
	
		#Initializing Fault: f25
		ft = StopRobot(mission.robots["r1"])
		self.faults.append(ft)
	
		#Initializing Fault: f26
		ft = ZeroRemainingEnergyCapacityReport(mission.goals["g3"].messages["m8"], 0.0) 
		self.faults.append(ft)
	
		#Initializing Fault: f27
		self.faults.append(ft)
	
		#Initializing Fault: f28
		self.faults.append(ft)
	
		#Initializing Fault: f29
		ft = DeactivateSensor(mission.robots["r3"].subcomponents["s5"]) 
		self.faults.append(ft)
	
		#Initializing Fault: f30
		ft = ZeroSpeed(mission.goals["g3"].messages["m9"], 0)
		self.faults.append(ft)

	def random_chunks(self, l):
		sp = np.random.choice(l - 2, (l // 10) - 1, replace=False) + 1
		sp.sort()
		return np.split([x for x in range(l)], sp)
	
	def reset_chunks(self):
		time_ranges = {}
		for fault in self.faults:
			time_ranges[fault.message.ID] = self.random_chunks(self.mission.duration)
		return time_ranges

	def generate_population(self, n):
		population = []
		for _ in range(n):
			time_ranges = self.reset_chunks()
			individual = []
			j = 0
			while j < 10:
				f = self.faults[random.randint(0, len(self.faults) - 1)]
				if time_ranges[f.message.ID] != None:
					if len(time_ranges[f.message.ID]) > 0:
						random.shuffle(time_ranges[f.message.ID])
						tmp = time_ranges[f.message.ID].pop()
						start = tmp[0]
						finish = tmp[len(tmp) - 1]
					else:
						start = 0
						finish = 0
					individual.append(Fault(copy.deepcopy(f), start, finish))
					j += 1
			population.append(individual)
		return population