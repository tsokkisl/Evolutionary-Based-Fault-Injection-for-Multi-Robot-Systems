from dsl.mission.Message import Message

class StopRobot:
    
    def __init__(self, robot):
        self.robot = robot
        self.message = Message("mStopRobot", "gid", "name", "sender", "receiver", "data")

    def exec_fault(self, mission, mrs):
        mission.robots[self.robot.ID].stop()
        mrs.robots[self.robot.ID].stop()

    def mutate(self):
        pass