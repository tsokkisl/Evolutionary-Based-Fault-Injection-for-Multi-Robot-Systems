class BlockMessage:
    
    def __init__(self, message, duration):
        self.message = message
        self.duration = duration

    def exec_fault(self, mission):
        pass
    
    def mutate(self):
        pass