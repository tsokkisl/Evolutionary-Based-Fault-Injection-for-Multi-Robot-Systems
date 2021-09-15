from gen.mission_loader import MissionLoader
from gen.sim_interface import SimInterface
import random
import time
from dsl.mission.Sensor import Sensor

class CI:
	
    goal_violations_per_goal = {}
    goals_last_violation_state = {}
    flag = True
    
    def __init__(self):
        # Setup Sim Interface
        print("--------------- Initilizing and starting sim interface ---------------\n")
        self.sim_interface = SimInterface()
        self.sim_interface.mission = MissionLoader().load_mission()
        self.sim_interface.ci = self
        self.sim_interface.daemon = True
        self.sim_interface.start()
        time.sleep(2)

    def reset_system_state(self, fs):
        self.fault_specification = fs
        self.sim_interface.mission = MissionLoader().load_mission()
        self.goal_violations_per_goal = {"g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0}
        self.goals_last_violation_state = {"g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False}
        self.time = 0

    def update_goal_violations(self, gid):
        if gid in self.goal_violations_per_goal.keys():
            self.goal_violations_per_goal[gid] += 1
        else:
            self.goal_violations_per_goal[gid] = 1

    def update_system_state(self):
        """ Update mission state """
        for robot in self.sim_interface.mission.robots.values():
            robot.update_position(self.sim_interface.get_POSITION(robot))
            robot.update_energy(self.sim_interface.get_ENERGY(robot))
            robot.update_speed(self.sim_interface.get_SPEED(robot))
            for sc in robot.subcomponents.values():
                if isinstance(sc, Sensor) and sc.state == "Active":
                    sample = self.sim_interface.get_sensor_sample(sc)
                    sc.samples.append(sample)
            """print('time={6}, position = [{0}, {1}, {2}], speed={3}, energy={4}, direction={5}'.format(robot.position.x, robot.position.y, 
            robot.position.z, robot.speed, robot.current_energy, robot.direction, self.time))
            print('--------------------------------')"""

    def execute_faults(self, time):
        """ Check for fault """
        for fault in self.fault_specification:
            fault.exec_fault(time, self.sim_interface.mission, self.sim_interface.mrs)
            	
    def run_single_objective_CI(self, fs):
        fitness = 0
        self.flag = True
        temp = []
        self.sim_interface.reset()
        self.sim_interface.mrs.reset()
        self.reset_system_state(fs)
        # Run simulation
        while self.flag:
            self.update_system_state()
            self.execute_faults(self.sim_interface.mrs.time)
            self.check_avoidCollision()
            self.check_stayWithinMissionArea()
            self.check_sufficientEnergy()
            self.check_gatherSamples_g4()
            self.check_gatherSamples_g5()
            self.check_gatherSamples_g6()
            self.goals_last_violation_state = {"g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False}
        for v in self.goal_violations_per_goal.values(): fitness += v
        fitness = fitness * 0.3 + (len(self.goal_violations_per_goal) * 10000) * 0.7
        for f in fs: temp.append({"Type": f.ft.__class__.__name__, "start": f.start, "finish": f.finish})
        temp.append(self.goal_violations_per_goal)
        temp.append(fitness)
        f = open('metrics.txt', 'a')
        f.write(str(temp) + '\n')
        f.close()
        return fitness
    
    def run_multi_objective_CI(self, fs, goals):
        self.goals = goals
        fitness = 0
        self.flag = True
        self.sim_interface.reset()
        self.sim_interface.mrs.reset()
        self.reset_system_state(fs)
        # Run simulation
        while self.flag:
            self.update_system_state()
            self.execute_faults(self.sim_interface.mrs.time)
            self.check_avoidCollision()
            self.check_stayWithinMissionArea()
            self.check_sufficientEnergy()
            self.check_gatherSamples_g4()
            self.check_gatherSamples_g5()
            self.check_gatherSamples_g6()
            self.goals_last_violation_state = {"g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False}
        #print(self.goal_violations_per_goal)
        if goals[0] not in self.goal_violations_per_goal.keys(): self.goal_violations_per_goal[goals[0]] = 0
        if goals[1] not in self.goal_violations_per_goal.keys(): self.goal_violations_per_goal[goals[1]] = 0
        with open('metrics.txt', 'a') as f:
            f.write(str(self.goal_violations_per_goal[goals[0]]) + ',' + str(self.goal_violations_per_goal[goals[1]]) + '\n')
            f.close()
        fitness = self.goal_violations_per_goal[goals[0]] + self.goal_violations_per_goal[goals[1]]
        return fitness
            
    def check_for_collision(self, p1, p2, r1, r2):
        return (p1[0] - r1 < p2[0] + r2 and p1[0] + r1 > p2[0] - r2 and p1[1] + r1 > p2[1] - r2 and p1[1] - r1 < p2[1] + r2)
                    
    def check_avoidCollision(self):
        # protected region User implemented method on begin
        goal_ID = "g1"
        is_violated = False
        """ Dependencies:  """
        """ Members: JEN KAL LEN  """
        """ Check if goal is violated and make a decision """
        collision_points = [[r.ID, r.position, 1] for r in self.sim_interface.mission.robots.values()] + [[o.ID, o.area.center, o.area.radius] for o in self.sim_interface.mission.obstacles.values()]
        for robot in self.sim_interface.mission.robots.values():
            collision = False
            for point in collision_points:
                if robot.ID != point[0] and self.check_for_collision(robot.position.get_coors(), point[1].get_coors(), 1, point[2]):
                    is_violated = True
                    collision = True
                    self.goals_last_violation_state[goal_ID] = True
                    break
            if not collision:
                d = robot.directions[random.randint(0, len(robot.directions) - 1)]
                robot.direction = d
                self.sim_interface.mrs.change_direction(robot, d)
            else:
                d = robot.avoid_collision()
                robot.direction = d
                self.sim_interface.mrs.change_direction(robot, d)
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_stayWithinMissionArea(self):
        # protected region User implemented method on begin
        goal_ID = "g2"
        is_violated = False
        """ Dependencies:  """
        """ Members: JEN KAL LEN  """
        """ Check if goal is violated and make a decision """
        for robot in self.sim_interface.mission.robots.values():
            if robot.distance_from_mission_center(self.sim_interface.mission.mission_area.center) > self.sim_interface.mission.mission_area.radius:
                is_violated = True
                d = robot.change_direction_towards_center(self.sim_interface.mission.mission_area.center)
                robot.direction = d
                self.sim_interface.mrs.change_direction(robot, d)
                self.goals_last_violation_state[goal_ID] = True
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_sufficientEnergy(self):
        # protected region User implemented method on begin
        goal_ID = "g3"
        is_violated = False
        """ Dependencies:  """
        """ Members: JEN KAL LEN  """
        """ Check if goal is violated and make a decision """
        for robot in self.sim_interface.mission.robots.values():
            if not robot.check_for_sufficient_energy():
                is_violated = True
                self.sim_interface.mission.robots[robot.ID].update_speed(random.randint(robot.speed // 2, (robot.speed // 2) + 1))
                self.goals_last_violation_state[goal_ID] = True
        if is_violated: self.update_goal_violations(goal_ID)
		# protected region User implemented method end
		
    def check_gatherSamples_g4(self):
        # protected region User implemented method on begin
        goal_ID = "g4"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        goal_area = self.sim_interface.mission.goals[goal_ID].goalArea.area
        robot = self.sim_interface.mission.robots[sensor.parent_ID]
        """ Dependencies:  """
        """ Members: JEN  """
        """ Check if goal is violated and make a decision """
        if sensor.state == "Active" and goal_area.center.distance(robot.position) <= goal_area.radius + 1:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
            d = robot.change_direction_towards_goal_area_center(goal_area)
            robot.direction = d
            self.sim_interface.mrs.change_direction(robot, d)
		# protected region User implemented method end
		
    def check_gatherSamples_g5(self):
        # protected region User implemented method on begin
        goal_ID = "g5"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        goal_area = self.sim_interface.mission.goals[goal_ID].goalArea.area
        robot = self.sim_interface.mission.robots[sensor.parent_ID]
        """ Dependencies:  """
        """ Members: KAL  """
        """ Check if goal is violated and make a decision """
        #print(sensor.state == "Active", self.goals_last_violation_state["g2"], goal_area.center.distance(robot.position) <= goal_area.radius + 1)
        if sensor.state == "Active" and goal_area.center.distance(robot.position) <= goal_area.radius + 1:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
            d = robot.change_direction_towards_goal_area_center(goal_area)
            robot.direction = d
            self.sim_interface.mrs.change_direction(robot, d)
		# protected region User implemented method end
		
    def check_gatherSamples_g6(self):
        # protected region User implemented method on begin
        goal_ID = "g6"
        sensor = self.sim_interface.mission.goals[goal_ID].goalTask.sensor
        goal_area = self.sim_interface.mission.goals[goal_ID].goalArea.area
        robot = self.sim_interface.mission.robots[sensor.parent_ID]
        """ Dependencies:  """
        """ Members: LEN  """
        """ Check if goal is violated and make a decision """
        if sensor.state == "Active" and goal_area.center.distance(robot.position) <= goal_area.radius + 1:
            if sensor.samples[len(sensor.samples) - 1] >= sensor.samples_per_second:
                g = self.sim_interface.mission.goals.get(goal_ID).goalTask
                g.total_samples += sensor.samples[len(sensor.samples) - 1]
        else:
            self.update_goal_violations(goal_ID)
            self.goals_last_violation_state[goal_ID] = True
            d = robot.change_direction_towards_goal_area_center(goal_area)
            robot.direction = d
            self.sim_interface.mrs.change_direction(robot, d)
		# protected region User implemented method end
		
