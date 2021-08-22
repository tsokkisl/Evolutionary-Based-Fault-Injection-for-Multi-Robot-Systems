from .GoalTask import GoalTask

class GatherSamples(GoalTask):
    
    total_samples = 0
    
    def __init__(self, tsn, s):
        self.target_sample_number = tsn
        self.sensor = s
        self.samples = []