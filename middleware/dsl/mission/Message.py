class Message:
	name = ""
	minFrequency = 0
	maxFrequency = 0
	head = ""
	
	def __init__(self, id, gid, name, sender, receiver, data):
		self.name = name
		self.sender = sender
		self.receiver = receiver
		self.data = data
		self.ID = id
		self.goal_ID = gid
	
	def is_to(self, c):
		return (self.receiver == c)
	
	def is_from(self, c):
		return (self.sender == c)
	
	def get_to(self):
		return self.receiver
	
	def get_from(self):
		return self.sender
	
	def get_name(self):
		return self.name
