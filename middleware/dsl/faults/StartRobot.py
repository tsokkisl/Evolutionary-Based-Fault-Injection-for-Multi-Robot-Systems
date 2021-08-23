from dsl.mission.Message import Message

class StartRobot:
    
    def __init__(self, robot):
        self.robot = robot
        self.message = Message("mStartRobot", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission):
        self.robot.start() 