from dsl.mission.GoalTask import GoalTask

class StayWithinMissionArea(GoalTask):
    def __init__(self, area):
        self.area = area