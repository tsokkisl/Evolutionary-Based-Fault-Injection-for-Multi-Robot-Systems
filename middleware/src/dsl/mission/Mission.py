class Mission:
	robots = {}
	computers = {}
	areas = {}
	objects = {} 
	obstacles = {}
	goals = {}
	
	def getGoals(self):
		return self.goals.values()
	
	def getGoal(self, id):
		return self.goals.get(id)
	
	def getNamedGoals(self):
		return self.goals
	
	def addGoal(self, id, goal):
		self.goals.put(id, goal)
	
	def getRobotNames(self, id):
		return self.robots.get(id)
	
	def getRobots(self):
		return self.robots
	
	def addRobot(self, id, robot):
		self.robots.put(id, robot)
		robot.checkPropertiesAndSetupState()
	
	def getAllSensorTypesOnVehicles(self):
		result = {}
		for robot in self.robots.values():
			for sensor in robot.getAllSensors():
				t = sensor.getType()
				result.put(t, robot)
		return result
	
	def getRobotNames(self):
		names = []
		for robot in self.getAllRobots():
			names.add(robot.getName())
		return names
	
	def getRobotSpeeds(self):
		robotSpeeds = {}
		for robot in self.getAllRobots():
			speed = robot.getDoubleComponentProperty("startSpeed")
			robotSpeeds.put(robot, speed)
		return robotSpeeds
	
	def getServer(self, name):
		return self.servers.get(name)
	
	def getServers(self):
		return self.servers.values()
	
	def addServer(self, id, server):
		self.servers.put(id, server)
	
	def getServerNames(self):
		names = []
		for server in self.getAllServers():
			names.add(server.getName())
		return names

	def getObstacleArea(self):
		return self.obstacleArea
	
	def setObstacleArea(self, area):
		self.obstacleArea = area
	
	def getMessage(self, msgName):
		return self.messages.get(msgName)
	
	def addMessage(self, msg):
		self.messages.put(msg.getName(), msg)
	
	def messagesToComponent(self, component):
		result = []
		for msg in self.messages.values():
			if msg.isTo(component):
				result.append(msg)
		return result
	
	def messagesFromComponent(self, component):
		result = []
		for msg in self.messages.values():
			if msg.isFrom(component):
				result.append(msg)
		return result
	
	def messagesToAnyComponent(self, components):
		result = []
		for msg in self.messages.values():
			if components.contains(msg.getTo()):
				result.append(msg)
		return result
	
	def messagesFromAnyComponent(self, components):
		result = []
		for msg in self.messages.values():
			if components.contains(msg.getFrom()):
				result.append(msg)
		return result