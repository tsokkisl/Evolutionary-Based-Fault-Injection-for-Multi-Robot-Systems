from dsl.mission.Message import Message

class StopRobot:
    
    def __init__(self, robot):
        self.robot = robot
        self.message = Message("mStopRobot", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission):
        self.robot.stop() 