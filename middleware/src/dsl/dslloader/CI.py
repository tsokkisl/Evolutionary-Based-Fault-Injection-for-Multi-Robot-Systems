from .mission_loader import MissionLoader

class CI:

    def __init__(self, m, fs):
        self.mission = m
        self.fault_specification = fs
        # Initialize system's state
        
    def reset_system_state(self, fs):
        self.fault_specification = fs
        # Reset system's state

    def runCI(self, fs):
        self.reset_system_state(fs)
        # Run simulation
    
    def gatherSamples(self):
        # protected region Insert Implementation on begin #
        pass
		# protected region Insert Implementation end #	
        
    def avoidCollision(self):
        # protected region Insert Implementation on begin #
        pass
		# protected region Insert Implementation end #	
        
    def sufficientEnergy(self):
        # protected region Insert Implementation on begin #
        pass
		# protected region Insert Implementation end #	
        
    def fixedDistanceBetweenRobots(self):
        # protected region Insert Implementation on begin #
        pass
		# protected region Insert Implementation end #	
        
