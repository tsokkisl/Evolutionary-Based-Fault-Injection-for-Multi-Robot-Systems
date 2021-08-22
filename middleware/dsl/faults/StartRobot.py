class StartRobot:
    
    def __init__(self, robot):
        self.robot = robot

    def run(self, mission):
        self.robot.start() 