from .mission_loader import MissionLoader
from ....core.sim_interface import SimInterface

class CI:
	
    def __init__(self, m, fs):
        self.mission = m
        self.fault_specification = fs
        self.sim_interface = SimInterface()
        # Initialize system's state
        
    def reset_system_state(self, fs):
        self.fault_specification = fs
        # Reset system's state

    def runCI(self, fs):
        self.reset_system_state(fs)
        # Run simulation
        for i in range(self.mission.duration):
            continue

    def gather_samples_g1000(self, sensor):
        # protected region User implemented method on begin
        goal_ID = "1000"
        s = self.mission.robots.get(sensor.parent_ID).sensors.get(sensor.ID)
        sample = self.sim_interface.get_sample(s)
        if sample != "NaN":
            g = self.mission.goals.get(goal_ID)
            g.total_samples += 1
            g.samples.append(sample)
		# protected region User implemented method end
		
    def avoid_collision(self):
        # protected region User implemented method on begin
        collision_points = [[r.ID, r.position] for r in self.mission.robots] + [[o.ID, o.area.center] for o in self.mission.obstacles]
        for robot in self.mission.robots:
            for point in collision_points:
                if robot.ID != point[0] and robot.position == point[1]:
                    robot.change_direction(robot.direction)
		# protected region User implemented method end
		
    def sufficient_energy(self):
        # protected region User implemented method on begin
        for robot in self.mission.robots:
            self.sim_interface.update_robot_position(robot.ID)
            self.sim_interface.update_robot_remaining_energy(robot.ID)
            if robot.check_for_sufficient_energy():
                for sensor in robot:
                    sensor.stop()
		# protected region User implemented method end

    def gather_samples_1004(self, sensor):
        # protected region User implemented method on begin
        goal_ID = "1004"
        s = self.mission.robots.get(sensor.parent_ID).sensors.get(sensor.ID)
        sample = self.sim_interface.get_sample(s)
        if sample != "NaN":
            g = self.mission.goals.get(goal_ID)
            g.total_samples += 1
            g.samples.append(sample)
		# protected region User implemented method end
	
    def stayWithinMissionArea(self):
        # protected region User implemented method on begin
        for robot in self.mission.robots:
            self.sim_interface.update_robot_position(robot.ID)
            if robot.distance_from_mission_center() > self.mission.area.radius:
                robot.change_direction(robot.direction)
		# protected region User implemented method end
		
