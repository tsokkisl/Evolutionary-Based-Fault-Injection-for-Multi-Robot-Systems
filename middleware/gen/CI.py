from gen.mission_loader import MissionLoader
from gen.sim_interface import SimInterface
import random
import time
from dsl.mission.Sensor import Sensor

class CI:
	
    total_goal_violations = [] 
    goal_violations_per_fault = {}
    goals_last_violation_state = {}
    time = 0
    
    def __init__(self):
        self.mission = MissionLoader().load_mission()
        # Setup Sim Interface
        print("--------------------------\nInitilising and starting sim interface\n--------------------------")
        self.sim_interface = SimInterface()
        self.sim_interface.daemon = True
        self.sim_interface.start()

    def reset_system_state(self, fs):
        self.mission = MissionLoader().load_mission()
        self.fault_specification = fs
        self.sim_interface.mission = self.mission
        self.total_goal_violations = [0 for _ in range(self.mission.duration)]
        self.goal_violations_per_fault = {}
        self.goals_last_violation_state = {"g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False}
        self.time = 0

    def update_goal_violations(self, gid):
        self.total_goal_violations[self.time] += 1
        if gid in self.goal_violations_per_fault.keys():
            self.goal_violations_per_fault[gid] += 1
        else:
            self.goal_violations_per_fault[gid] = 1

    def update_system_state(self):
        """ Update mission state """
        for robot in self.mission.robots.values():
            robot.update_position(self.sim_interface.get_POSITION(robot))
            robot.update_energy(self.sim_interface.get_ENERGY(robot))
            robot.update_speed(self.sim_interface.get_SPEED(robot))
            for sc in robot.subcomponents.values():
                if isinstance(sc, Sensor) and sc.state == "Active":
                    sample = self.sim_interface.get_sensor_sample(sc)
                    sc.samples.append(sample)
            #print('time={6}, position = [{0}, {1}, {2}], speed={3}, energy={4}, direction={5}'.format(robot.position.x, robot.position.y, 
            #robot.position.z, robot.speed, robot.current_energy, robot.direction, self.time))
            #print('--------------------------------')

    def execute_faults(self):
        """ Check for fault """
        for fault in self.fault_specification:
            fault.exec_fault(self.time, self.sim_interface.mission, self.sim_interface.mrs)
            	
    def runCI(self, fs):
        self.reset_system_state(fs)
        # Run simulation
        for t in range(self.mission.duration):
        	self.update_system_state()
        	self.execute_faults()
        	self.check_avoidCollision()
        	self.check_stayWithinMissionArea()
        	self.check_sufficientEnergy()
        	self.check_gathersamples_g4()
        	self.check_gatherSamples_g5()
        	self.check_gatherSamples_g6()
        	t += 1
        	self.time = t
        	#time.sleep(1)
        	self.goals_last_violation_state = {"g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False}
        print(self.goal_violations_per_fault)
        #print(self.total_goal_violations)
    
    def check_for_collision(self, p1, p2, r1, r2):
        return (p1[0] - r1 < p2[0] + r2 and p1[0] + r1 > p2[0] - r2 and p1[1] + r1 > p2[1] - r2 and p1[1] - r1 < p2[1] + r2)
                    
    def check_avoidCollision(self):
        # protected region User implemented method on begin
        goal_ID = "g1"
        is_violated = False
        """ Check if goal is violated and make a decision """
        collision_points = [[r.ID, r.position, 1] for r in self.sim_interface.mission.robots.values()] + [[o.ID, o.area.center, o.area.radius] for o in self.sim_interface.mission.obstacles.values()]
        for robot in self.sim_interface.mission.robots.values():
            collision = False
            for point in collision_points:
                if robot.ID != point[0] and self.check_for_collision(robot.position.get_coors(), point[1].get_coors(), 1, point[2]):
                    is_violated = True
                    d = robot.avoid_collision()
                    self.sim_interface.mrs.change_direction(robot, d)
                    self.goals_last_violation_state[goal_ID] = True
                    collision = True
                    break
            if not collision:
                d = robot.directions[random.randint(0, len(robot.directions) - 1)]
                robot.direction = d
                self.sim_interface.mrs.change_direction(robot, d)
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_stayWithinMissionArea(self):
        # protected region User implemented method on begin
        goal_ID = "g2"
        is_violated = False
        """ Check if goal is violated and make a decision """
        for robot in self.sim_interface.mission.robots.values():
            if robot.distance_from_mission_center(self.sim_interface.mission.mission_area.center) > self.sim_interface.mission.mission_area.radius:
                is_violated = True
                d = robot.change_direction_towards_center()
                self.sim_interface.mrs.change_direction(robot, d)
                self.goals_last_violation_state[goal_ID] = True
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_sufficientEnergy(self):
        # protected region User implemented method on begin
        goal_ID = "g3"
        is_violated = False
        """ Check if goal is violated and make a decision """
        for robot in self.sim_interface.mission.robots.values():
            if not robot.check_for_sufficient_energy():
                is_violated = True
                self.sim_interface.mission.robots[robot.ID].update_speed(random.randint(robot.speed // 2, (robot.speed // 2) + 1))
                self.goals_last_violation_state[goal_ID] = True
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_gathersamples_g4(self):
        # protected region User implemented method on begin
        goal_ID = "g4"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        """ Check if goal is violated and make a decision """
        if sensor.state == "Active" and self.goals_last_violation_state["g3"] and self.goals_last_violation_state["g2"]:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
		# protected region User implemented method end
		
    def check_gatherSamples_g5(self):
        # protected region User implemented method on begin
        goal_ID = "g5"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        """ Check if goal is violated and make a decision """
        if sensor.state == "Active" and self.goals_last_violation_state["g3"] and self.goals_last_violation_state["g2"]:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
		# protected region User implemented method end
		
    def check_gatherSamples_g6(self):
        # protected region User implemented method on begin
        goal_ID = "g6"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        """ Check if goal is violated and make a decision """
        if sensor.state == "Active" and self.goals_last_violation_state["g3"] and self.goals_last_violation_state["g2"]:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
		# protected region User implemented method end
		
    
    """
    def print_mission_and_fault_specification(self):
        self.reset_system_state(FaultSpecification(MissionLoader().load_mission()))
        # Setup mission specification
        print("Mission Specification")
        print(self.mission.name)
        print(self.mission.duration)
        print(self.mission.mission_area)
        print(self.mission.robots)
        print(self.mission.servers)
        print(self.mission.obstacles)
        print(self.mission.goals)

        print("\nFault Specification")
        print(self.fault_specification.faults)
        pop = self.fault_specification.generate_population()
        for i in range(len(pop)):
            s = ""
            print("INDIVIDUAL: " + str(i))
            for k in pop[i]:
                s += k.type.message.ID + "(" + str(k.start) + ", " + str(k.finish)+ ") "
            print(s)
            print("---------------------------------\n")
     """