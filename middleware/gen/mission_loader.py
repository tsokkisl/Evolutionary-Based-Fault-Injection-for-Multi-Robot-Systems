from dsl.mission.Mission import Mission
from dsl.mission.Server import Server
from dsl.mission.Battery import Battery
from dsl.mission.Robot import Robot
from dsl.mission.Coordinates import Coordinates
from dsl.mission.Sensor import Sensor
from dsl.mission.Goal import Goal
from dsl.mission.GoalMembers import GoalMembers
from dsl.mission.Area import Area
from dsl.mission.GoalArea import GoalArea
from dsl.mission.Message import Message
from dsl.mission.GatherSamples import GatherSamples
from dsl.mission.SufficientEnergy import SufficientEnergy
from dsl.mission.AvoidCollision import AvoidCollision
from dsl.mission.FixedDistance import FixedDistance
from dsl.mission.MotionSource import MotionSource
from dsl.mission.Obstacle import Obstacle
from dsl.mission.StayWithinMissionArea import StayWithinMissionArea
from dsl.mission.GoalDependencies import GoalDependencies

class MissionLoader:
	def load_mission(self):
		mission_area = Area(Coordinates(0, 0, 0), 2000)	
		self.mission = Mission("1000", 1000.0, mission_area)
	
		# Initilize Server: sv1
		s1 = Server("sv1", "sv1")
		self.mission.add_server("sv1", s1)
	
		# Initilize Robot: LEN
		subcomponents = []
		# Initilize Robot: LEN's subcomponents
		sensor_s1 = Sensor("s1", "r1", "GPS_POSITION", 2.0, 5)
		subcomponents.append(sensor_s1)
		sensor_s2 = Sensor("s2", "r1", "PRESSURE", 2.0, 5)
		subcomponents.append(sensor_s2)
		motion_source_ms1 = MotionSource("ms1", 5.0)
		subcomponents.append(motion_source_ms1)
		battery_b1 = Battery("b1", 20000.0)
		subcomponents.append(battery_b1)
		battery_b2 = Battery("b2", 80000.0)
		subcomponents.append(battery_b2)
		robot_r1 = Robot("r1", "LEN", 5, Coordinates(250, -250, 1), subcomponents)
		robot_r1.configure_robot()
		sensor_s1.set_parent(robot_r1)
		sensor_s2.set_parent(robot_r1)
		self.mission.add_robot("r1", robot_r1)
	
		# Initilize Robot: JEN
		subcomponents = []
		# Initilize Robot: JEN's subcomponents
		sensor_s3 = Sensor("s3", "r2", "GPS_POSITION", 2.0, 5)
		subcomponents.append(sensor_s3)
		sensor_s4 = Sensor("s4", "r2", "TEMPERATURE", 2.0, 5)
		subcomponents.append(sensor_s4)
		motion_source_ms2 = MotionSource("ms2", 5.0)
		subcomponents.append(motion_source_ms2)
		battery_b3 = Battery("b3", 4000.0)
		subcomponents.append(battery_b3)
		battery_b4 = Battery("b4", 60000.0)
		subcomponents.append(battery_b4)
		robot_r2 = Robot("r2", "JEN", 4, Coordinates(-250, 250, 1), subcomponents)
		robot_r2.configure_robot()
		sensor_s3.set_parent(robot_r2)
		sensor_s4.set_parent(robot_r2)
		self.mission.add_robot("r2", robot_r2)
	
		# Initilize Robot: KAL
		subcomponents = []
		# Initilize Robot: KAL's subcomponents
		sensor_s5 = Sensor("s5", "r3", "GPS_POSITION", 2.0, 5)
		subcomponents.append(sensor_s5)
		sensor_s6 = Sensor("s6", "r3", "DEPTH", 2.0, 5)
		subcomponents.append(sensor_s6)
		motion_source_ms3 = MotionSource("ms3", 5.0)
		subcomponents.append(motion_source_ms3)
		battery_b5 = Battery("b5", 50000.0)
		subcomponents.append(battery_b5)
		battery_b6 = Battery("b6", 50000.0)
		subcomponents.append(battery_b6)
		robot_r3 = Robot("r3", "KAL", 4, Coordinates(250, 250, 1), subcomponents)
		robot_r3.configure_robot()
		sensor_s5.set_parent(robot_r3)
		sensor_s6.set_parent(robot_r3)
		self.mission.add_robot("r3", robot_r3)
	
	
		# Initilize Goal: AvoidCollision
		members = []
		members.append(self.mission.robots.get("r2"))
		members.append(self.mission.robots.get("r3"))
		members.append(self.mission.robots.get("r1"))
		goal_members_g1 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g1 = GoalDependencies(g_deps)
		rbts = []
		obs = []
		rbts.append(self.mission.robots.get("r2"))
		rbts.append(self.mission.robots.get("r3"))
		rbts.append(self.mission.robots.get("r1"))
		obs.append(self.mission.obstacles.get("o1"))
		obs.append(self.mission.obstacles.get("o2"))
		obs.append(self.mission.obstacles.get("o3"))
		obs.append(self.mission.obstacles.get("o4"))
		obs.append(self.mission.obstacles.get("o5"))
		obs.append(self.mission.obstacles.get("o6"))
		obs.append(self.mission.obstacles.get("o7"))
		obs.append(self.mission.obstacles.get("o8"))
		goal_task_g1 = AvoidCollision(rbts, obs)
		goal_area_g1 = GoalArea(Area(Coordinates(600, -200, 0), 4))
		goal_messages = []
		sender = self.mission.robots.get("r2")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m1 = Message("m1", "g1", "h", sender, receiver, data)
		goal_messages.append(msg_m1) 
		sender = self.mission.robots.get("r3")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m2 = Message("m2", "g1", "h", sender, receiver, data)
		goal_messages.append(msg_m2) 
		sender = self.mission.robots.get("r1")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m3 = Message("m3", "g1", "h", sender, receiver, data)
		goal_messages.append(msg_m3) 
		goal_g1 = Goal("AvoidCollision", self.mission, goal_dependecies_g1, goal_members_g1, goal_area_g1, goal_task_g1, goal_messages)
		self.mission.add_goal("g1", goal_g1)	
	
		# Initilize Goal: StayWithinMissionArea
		members = []
		members.append(self.mission.robots.get("r2"))
		members.append(self.mission.robots.get("r3"))
		members.append(self.mission.robots.get("r1"))
		goal_members_g2 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g2 = GoalDependencies(g_deps)
		goal_task_g2 = StayWithinMissionArea(Area(Coordinates(0, 0, 0), 2000))
		goal_area_g2 = GoalArea(Area(Coordinates(-800, 450, 1), 11))
		goal_messages = []
		sender = self.mission.robots.get("r2")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m4 = Message("m4", "g2", "h", sender, receiver, data)
		goal_messages.append(msg_m4) 
		sender = self.mission.robots.get("r3")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m5 = Message("m5", "g2", "h", sender, receiver, data)
		goal_messages.append(msg_m5) 
		sender = self.mission.robots.get("r1")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		msg_m6 = Message("m6", "g2", "h", sender, receiver, data)
		goal_messages.append(msg_m6) 
		goal_g2 = Goal("StayWithinMissionArea", self.mission, goal_dependecies_g2, goal_members_g2, goal_area_g2, goal_task_g2, goal_messages)
		self.mission.add_goal("g2", goal_g2)	
	
		# Initilize Goal: SufficientEnergy
		members = []
		members.append(self.mission.robots.get("r2"))
		members.append(self.mission.robots.get("r3"))
		members.append(self.mission.robots.get("r1"))
		goal_members_g3 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g3 = GoalDependencies(g_deps)
		goal_task_g3 = SufficientEnergy()
		goal_area_g3 = GoalArea(Area(Coordinates(0, 0, 0), 1000))
		goal_messages = []
		sender = self.mission.robots.get("r2")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		data.append(["SPEED", "Int"])
		data.append(["ENERGY", "Double"])
		msg_m7 = Message("m7", "g3", "h", sender, receiver, data)
		goal_messages.append(msg_m7) 
		sender = self.mission.robots.get("r3")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		data.append(["SPEED", "Int"])
		data.append(["ENERGY", "Double"])
		msg_m8 = Message("m8", "g3", "h", sender, receiver, data)
		goal_messages.append(msg_m8) 
		sender = self.mission.robots.get("r1")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["POSITION", "Coordinates"])
		data.append(["SPEED", "Int"])
		data.append(["ENERGY", "Double"])
		msg_m9 = Message("m9", "g3", "h", sender, receiver, data)
		goal_messages.append(msg_m9) 
		goal_g3 = Goal("SufficientEnergy", self.mission, goal_dependecies_g3, goal_members_g3, goal_area_g3, goal_task_g3, goal_messages)
		self.mission.add_goal("g3", goal_g3)	
	
		# Initilize Goal: GatherSamples
		members = []
		members.append(self.mission.robots.get("r2"))
		goal_members_g4 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g4 = GoalDependencies(g_deps)
		s = self.mission.robots["r2"].subcomponents["s4"]
		goal_task_g4 = GatherSamples(250, s)
		goal_area_g4 = GoalArea(Area(Coordinates(-250, 250, 1), 150))
		goal_messages = []
		sender = self.mission.robots.get("r2")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["TEMPERATURE", "Int"])
		msg_m10 = Message("m10", "g4", "h", sender, receiver, data)
		goal_messages.append(msg_m10) 
		goal_g4 = Goal("GatherSamples", self.mission, goal_dependecies_g4, goal_members_g4, goal_area_g4, goal_task_g4, goal_messages)
		self.mission.add_goal("g4", goal_g4)	
	
		# Initilize Goal: GatherSamples
		members = []
		members.append(self.mission.robots.get("r3"))
		goal_members_g5 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g5 = GoalDependencies(g_deps)
		s = self.mission.robots["r3"].subcomponents["s6"]
		goal_task_g5 = GatherSamples(400, s)
		goal_area_g5 = GoalArea(Area(Coordinates(250, 250, 1), 150))
		goal_messages = []
		sender = self.mission.robots.get("r3")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["DEPTH", "Double"])
		msg_m11 = Message("m11", "g5", "h", sender, receiver, data)
		goal_messages.append(msg_m11) 
		goal_g5 = Goal("GatherSamples", self.mission, goal_dependecies_g5, goal_members_g5, goal_area_g5, goal_task_g5, goal_messages)
		self.mission.add_goal("g5", goal_g5)	
	
		# Initilize Goal: GatherSamples
		members = []
		members.append(self.mission.robots.get("r1"))
		goal_members_g6 = GoalMembers(members, self.mission)		
		g_deps = []
		goal_dependecies_g6 = GoalDependencies(g_deps)
		s = self.mission.robots["r1"].subcomponents["s2"]
		goal_task_g6 = GatherSamples(500, s)
		goal_area_g6 = GoalArea(Area(Coordinates(250, -250, 1), 150))
		goal_messages = []
		sender = self.mission.robots.get("r1")
		receiver = self.mission.servers.get("sv1")
		data = []
		data.append(["PRESSURE", "Double"])
		msg_m12 = Message("m12", "g6", "h", sender, receiver, data)
		goal_messages.append(msg_m12) 
		goal_g6 = Goal("GatherSamples", self.mission, goal_dependecies_g6, goal_members_g6, goal_area_g6, goal_task_g6, goal_messages)
		self.mission.add_goal("g6", goal_g6)	
	
		# Initilize Obstacle: o1
		obstacle_o1 = Obstacle("o1", Area(Coordinates(0, 500, 1), 50))
		self.mission.add_obstacle("o1", obstacle_o1)	
	
		# Initilize Obstacle: o2
		obstacle_o2 = Obstacle("o2", Area(Coordinates(500, 500, 1), 40))
		self.mission.add_obstacle("o2", obstacle_o2)	
	
		# Initilize Obstacle: o3
		obstacle_o3 = Obstacle("o3", Area(Coordinates(500, 0, 1), 45))
		self.mission.add_obstacle("o3", obstacle_o3)	
	
		# Initilize Obstacle: o4
		obstacle_o4 = Obstacle("o4", Area(Coordinates(500, -500, 1), 25))
		self.mission.add_obstacle("o4", obstacle_o4)	
	
		# Initilize Obstacle: o5
		obstacle_o5 = Obstacle("o5", Area(Coordinates(0, -500, 1), 30))
		self.mission.add_obstacle("o5", obstacle_o5)	
	
		# Initilize Obstacle: o6
		obstacle_o6 = Obstacle("o6", Area(Coordinates(-500, -500, 1), 28))
		self.mission.add_obstacle("o6", obstacle_o6)	
	
		# Initilize Obstacle: o7
		obstacle_o7 = Obstacle("o7", Area(Coordinates(-500, 0, 1), 45))
		self.mission.add_obstacle("o7", obstacle_o7)	
	
		# Initilize Obstacle: o8
		obstacle_o8 = Obstacle("o8", Area(Coordinates(-500, 500, 1), 15))
		self.mission.add_obstacle("o8", obstacle_o8)	
	
		return self.mission