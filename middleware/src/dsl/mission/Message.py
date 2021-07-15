class Message:
	name = ""
	sender = []
	receiver = []
	minFrequency = 0
	maxFrequency = 0
	head = ""
	data = []
	
	def __init__(self, name, type):
		self.name = name
	
	def __init__(self, name, fromSingle, toSingle, data):
		self.name = name
		self.sender.add(fromSingle)
		self.receiver.add(toSingle)
		self.data = data
	
	def __init__(self, name, fromMultiple, toSingle, data):
		self.name = name
		self.sender.addAll(fromMultiple)
		self.receiver.add(toSingle)
		self.data = data
	
	def __init__(self, name, type, fromMultiple, toMultiple, data):
		self.name = name
		self.sender.addAll(fromMultiple)
		self.receiver.addAll(toMultiple)
		self.data = data
		self.type = type
	
	def __init__(self, name, fromSingle, toMultiple, data):
		self.name = name
		self.sender.add(fromSingle)
		self.receiver.addAll(toMultiple)
		self.data = data
	
	def isTo(self, c):
		return (self.receiver == c)
	
	def isFrom(self, c):
		return (self.sender == c)
	
	def getTo(self):
		return self.receiver
	
	def getFrom(self):
		return self.sender
	
	def getName(self):
		return self.name
