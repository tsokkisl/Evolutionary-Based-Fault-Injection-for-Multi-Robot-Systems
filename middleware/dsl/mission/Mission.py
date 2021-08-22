class Mission:

	robots = {}
	servers = {}
	obstacles = {}
	goals = {}
	
	def __init__(self, n, d, m):
		self.name = n
		self.duration = int(d)
		self.mission_area = m
	
	def get_goals(self):
		return self.goals.values()
	
	def get_goal(self, id):
		return self.goals.get(id)
	
	def get_named_goals(self):
		return self.goals
	
	def add_goal(self, id, goal):
		self.goals[id] = goal
	
	def get_robot_names(self, id):
		return self.robots.get(id)
	
	def get_robots(self):
		return self.robots
	
	def add_robot(self, id, robot):
		self.robots[id] = robot
	
	def add_obstacle(self, id, obstacle):
		self.obstacles[id] = obstacle

	def get_obstacles(self):
		return self.obstacles

	def getAllSensorTypesOnVehicles(self):
		result = {}
		for robot in self.robots.values():
			for sensor in robot.getAllSensors():
				t = sensor.getType()
				result[t] = robot
		return result
	
	def getRobotNames(self):
		names = []
		for robot in self.getAllRobots():
			names.add(robot.getName())
		return names
	
	def get_robot_speeds(self):
		robotSpeeds = {}
		for robot in self.getAllRobots():
			speed = robot.getDoubleComponentProperty("startSpeed")
			robotSpeeds[robot.ID] = speed
		return robotSpeeds
	
	def get_server(self, name):
		return self.servers.get(name)
	
	def get_servers(self):
		return self.servers.values()
	
	def add_server(self, id, server):
		self.servers[id] = server
	
	def get_server_names(self):
		names = []
		for server in self.getAllServers():
			names.add(server.getName())
		return names

	def get_abstacle_area(self):
		return self.obstacleArea
	
	def set_obstacle_area(self, area):
		self.obstacleArea = area
	
	def get_essage(self, msgName):
		return self.messages.get(msgName)
	
	def add_message(self, msg):
		self.messages[msg.getName()] = msg
	
	def messages_to_component(self, component):
		result = []
		for msg in self.messages.values():
			if msg.isTo(component):
				result.append(msg)
		return result
	
	def messages_from_component(self, component):
		result = []
		for msg in self.messages.values():
			if msg.isFrom(component):
				result.append(msg)
		return result
	
	def messages_to_any_component(self, components):
		result = []
		for msg in self.messages.values():
			if components.contains(msg.getTo()):
				result.append(msg)
		return result
	
	def messages_from_any_component(self, components):
		result = []
		for msg in self.messages.values():
			if components.contains(msg.getFrom()):
				result.append(msg)
		return result