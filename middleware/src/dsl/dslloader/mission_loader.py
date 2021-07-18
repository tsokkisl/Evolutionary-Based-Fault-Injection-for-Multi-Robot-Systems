from ..mission import *

class MissionLoader:
	def loadMission(self):
	
		self.mission = Mission()
	
		# Initilize Server: TIM
		s1 = Server("s1000", "TIM")
		self.mission.addServer("s1000")
		# Initilize Robot: SAM
		robot_r1000 = Robot("r1000", "SAM")
		robot_r1000.setDoubleComponentProperty("SPEED", 200.0)
		robot_r1000.setIntComponentProperty("ENERGY", 2000)
		robot_r1000.setCoordinateComponentProperty("startLocation", Coordinate(1, 2, -1))	
		# Initilize Robot: SAM's subcomponents
		battery_b1000 = Battery()
		robot_r1000.addSubcomponent("b1000", battery_b1000)
	
		cpu_c1000 = CPU()
		robot_r1000.addSubcomponent("c1000", cpu_c1000)
	
		sensor_s1000 = Sensor("s1000", "GPS_POSITION")
		sensor_s1000.setParent(robot_r1000)
		robot_r1000.addSubcomponent("s1000", sensor_s1000)
	
		sensor_s1001 = Sensor("s1001", "TEMPERATURE")
		sensor_s1001.setParent(robot_r1000)
		robot_r1000.addSubcomponent("s1001", sensor_s1001)
	
		self.mission.addRobot("r1000", robot_r1000)
		# Initilize Robot: TOM
		robot_r1001 = Robot("r1001", "TOM")
		robot_r1001.setDoubleComponentProperty("SPEED", 100.0)
		robot_r1001.setIntComponentProperty("ENERGY", 4000)
		robot_r1001.setCoordinateComponentProperty("startLocation", Coordinate(0, 2, 0))	
		# Initilize Robot: TOM's subcomponents
		battery_b1001 = Battery()
		robot_r1001.addSubcomponent("b1001", battery_b1001)
	
		cpu_c1001 = CPU()
		robot_r1001.addSubcomponent("c1001", cpu_c1001)
	
		sensor_s1002 = Sensor("s1002", "PRESSURE")
		sensor_s1002.setParent(robot_r1001)
		robot_r1001.addSubcomponent("s1002", sensor_s1002)
	
		sensor_s1003 = Sensor("s1003", "GPS_POSITION")
		sensor_s1003.setParent(robot_r1001)
		robot_r1001.addSubcomponent("s1003", sensor_s1003)
	
		self.mission.addRobot("r1001", robot_r1001)
	
		# Initilize Goal: Gather_samples
		members = []
		members.append(self.mission.robots.get("r1000"))
		goal_members_g1000 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g1000 = []	
		s = self.mission.sensors.get("s1001")
		goal_task_g1000 = GatherSamples(100, 200, s)
		goal_area_g1000 = GoalArea(Area(Coordinate(5, 5, 5), 1))

		goal_messages = []
		sender = self.mission.robots.get("r1000")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1000 = Message("TEMPERATURE", sender, receiver, data)
		goal_messages.append(msg_m1000) 
		goal_g1000 = Goal("Gather_samples", self.mission, goal_dependecies_g1000, goal_members_g1000, goal_area_g1000, goal_task_g1000, goal_messages)
		self.mission.addGoal("g1000", goal_g1000)	
		# Initilize Goal: Avoid_collision
		members = []
		members.append(self.mission.robots.get("r1000"))
		members.append(self.mission.robots.get("r1001"))
		goal_members_g1001 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g1001 = []	
		rbts = []
		obs = []
		rbts.append(self.mission.robots.get("r1000"))
		rbts.append(self.mission.robots.get("r1001"))
		obs.append(self.mission.obstacles.get("o1000"))
		obs.append(self.mission.obstacles.get("o1001"))
		goal_task_g1001 = AvoidCollision(rbts, obs)
		goal_area_g1001 = GoalArea(Area(Coordinate(0, 0, 0), 1))

		goal_messages = []
		sender = self.mission.robots.get("r1000")
		receiver = self.mission.robots.get("r1001")
		data = []
		msg_m1001 = Message("COORDINATES", sender, receiver, data)
		goal_messages.append(msg_m1001) 
		sender = self.mission.robots.get("r1001")
		receiver = self.mission.robots.get("r1000")
		data = []
		msg_m1002 = Message("COORDINATES", sender, receiver, data)
		goal_messages.append(msg_m1002) 
		goal_g1001 = Goal("Avoid_collision", self.mission, goal_dependecies_g1001, goal_members_g1001, goal_area_g1001, goal_task_g1001, goal_messages)
		self.mission.addGoal("g1001", goal_g1001)	
		# Initilize Goal: Sufficient_energy
		members = []
		members.append(self.mission.robots.get("r1000"))
		members.append(self.mission.robots.get("r1001"))
		goal_members_g1002 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g1002 = []	
		goal_task_g1002 = SufficientEnergy()
		goal_area_g1002 = GoalArea(Area(Coordinate(1, 2, 2), 10))

		goal_messages = []
		sender = self.mission.robots.get("r1000")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1003 = Message("ENERGY", sender, receiver, data)
		goal_messages.append(msg_m1003) 
		sender = self.mission.robots.get("r1001")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1004 = Message("ENERGY", sender, receiver, data)
		goal_messages.append(msg_m1004) 
		goal_g1002 = Goal("Sufficient_energy", self.mission, goal_dependecies_g1002, goal_members_g1002, goal_area_g1002, goal_task_g1002, goal_messages)
		self.mission.addGoal("g1002", goal_g1002)	
		# Initilize Goal: Fixed_distance_between_robots
		members = []
		members.append(self.mission.robots.get("r1000"))
		members.append(self.mission.robots.get("r1001"))
		goal_members_1003 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_1003 = []	
		goal_task_1003 = FixedDistance(5)
		goal_area_1003 = GoalArea(Area(Coordinate(0, -2, -8), 2))

		goal_messages = []
		sender = self.mission.robots.get("r1000")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1005 = Message("COORDINATES", sender, receiver, data)
		goal_messages.append(msg_m1005) 
		sender = self.mission.robots.get("r1001")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1006 = Message("COORDINATES", sender, receiver, data)
		goal_messages.append(msg_m1006) 
		goal_1003 = Goal("Fixed_distance_between_robots", self.mission, goal_dependecies_1003, goal_members_1003, goal_area_1003, goal_task_1003, goal_messages)
		self.mission.addGoal("1003", goal_1003)	
		# Initilize Goal: Gather_samples
		members = []
		members.append(self.mission.robots.get("r1001"))
		goal_members_1004 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_1004 = []	
		s = self.mission.sensors.get("s1003")
		goal_task_1004 = GatherSamples(200, 900, s)
		goal_area_1004 = GoalArea(Area(Coordinate(0, 0, 0), 8))

		goal_messages = []
		sender = self.mission.servers.get("s1003")
		receiver = self.mission.servers.get("s1000")
		data = []
		msg_m1008 = Message("TEMPERATURE", sender, receiver, data)
		goal_messages.append(msg_m1008) 
		goal_1004 = Goal("Gather_samples", self.mission, goal_dependecies_1004, goal_members_1004, goal_area_1004, goal_task_1004, goal_messages)
		self.mission.addGoal("1004", goal_1004)	
		return self.mission