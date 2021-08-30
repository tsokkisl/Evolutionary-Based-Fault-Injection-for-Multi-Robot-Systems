from time import process_time
from dsl.mission.Component import Component
from dsl.mission.Coordinates import Coordinates
from dsl.mission.Sensor import Sensor
from dsl.mission.MotionSource import MotionSource
from dsl.mission.Battery import Battery
import random
import math

class Robot(Component):
    moves = {"NORTH": [0, 1, 0], "EAST": [1, 0, 0], "WEST": [-1, 0, 0], "SOUTH": [0, -1, 0], "NORTH_EAST": [1, 1, 0], "NORTH_WEST": [-1, 1, 0], "SOUTH_EAST": [1, -1, 0], "SOUTH_WEST": [-1, -1, 0]}
    directions = ["NORTH", "EAST", "WEST", "SOUTH", "NORTH_EAST", "NORTH_WEST", "SOUTH_EAST", "SOUTH_WEST"]

    def __init__(self, id, name, speed, position, subcomponents):
        super().__init__()
        self.current_energy = 0
        self.starting_energy = 0
        self.direction = "NORTH"
        self.name = name
        self.ID = id
        self.speed = speed
        self.position = position
        self.subcomponents = {}
        for sc in subcomponents:
            self.add_subcomponent(sc.ID, sc)
        self.starting_position = position

    def add_subcomponent(self, id, subcomponent):
        self.subcomponents[id] = subcomponent

    def configure_robot(self):
        self.setup_initial_state()

    def get_name(self):
        return self.name

    def get_robot_type(self):
        return self.type
    
    def get_sensor_of_type(self, sensor_type):
        sensors = []
        for sc in self.subcomponents:
            if isinstance(sc, Sensor) and sc.sensorType == sensor_type:
                sensors.add(sc)
        return sensors

    def get_all_sensors(self):
        sensors = []
        for sc in self.subcomponents.values():
            if isinstance(sc, Sensor):
                sensors.append(sc)
        return sensors

    def get_all_motion_sources(self):
        ms = []
        for sc in self.subcomponents.values():
            if isinstance(sc, MotionSource):
                ms.append(sc)
        return ms

    def get_all_batteries(self):
        batteries = []
        for sc in self.subcomponents.values():
            if isinstance(sc, Battery):
                batteries.append(sc)
        return batteries

    def set_energy_capacity(self):
        for b in self.get_all_batteries():
            self.current_energy += b.get_total_energy()
            self.starting_energy += b.get_total_energy()

    def get_remaining_energy(self):
        return self.current_energy

    def out_of_energy(self):
        return self.current_energy <= 0.0

    def deplete_energy(self, energy):
        self.current_energy -= energy
        self.current_energy = max(self.current_energy, 0.0)
        if self.current_energy <= 0.0:
            self.speed = 0

    def register_energy_usage(self, prev_location):
        energy_required = 0.0
        current_location = self.position
        d = current_location.distance(prev_location)
        for motion_source in self.get_all_motion_sources():
            energy_required += motion_source.get_energy_per_distance_unit() * d
        self.deplete_energy(energy_required)
    
    def setup_initial_state(self):
        self.set_energy_capacity()

    def change_direction_towards_center(self):
        mv = self.moves[self.directions[0]]
        min = self.position.distance(Coordinates(mv[0] * self.speed + self.position.get_x(), mv[1] * self.speed + self.position.get_y(), mv[2] * self.speed + self.position.get_z()))
        for d in self.directions:
            next_position = Coordinates(self.moves[d][0] * self.speed + self.position.get_x(), self.moves[d][1] * self.speed + self.position.get_y(), self.moves[d][2] * self.speed + self.position.get_z())
            if self.position.distance(next_position) < min:
                min = next_position
                self.direction = d
        return self.direction

    def check_for_collision(self, p1, p2, r1, r2):
        return (p1[0] - r1 < p2[0] + r2 and p1[0] + r1 > p2[0] - r2 and p1[1] + r1 > p2[1] - r2 and p1[1] - r1 < p2[1] + r2)

    def avoid_collision(self):
        #opposite_directions = {"NORTH": "SOUTH", "EAST": "WEST", "WEST": "EAST", "SOUTH": "NORTH", "NORTH_EAST": "SOUTH_WEST", 
        #"NORTH_WEST": "SOUTH_EAST", "SOUTH_EAST": "NORTH_WEST", "SOUTH_WEST": "NORTH_EAST"}
        valid_directions = []
        for d in self.directions:
            next_position = Coordinates((self.moves[d][0] * self.speed) + self.position.get_x(), (self.moves[d][1] * self.speed) + self.position.get_y(), (self.moves[d][2] * self.speed) + self.position.get_z())
            if not self.check_for_collision(self.position.get_coors(), next_position.get_coors(), 1, 1): valid_directions.append(d)
        if len(valid_directions) > 0:
            self.direction = valid_directions[random.randint(0, len(valid_directions) - 1)]
        return self.direction

    def check_if_sufficient_energy(self):
        m = self.moves[self.direction]
        energy_required = 0.0
        next_position = Coordinates((m[0] * self.speed) + self.position.get_x(), (m[1] * self.speed) 
        + self.position.get_y(), (m[2] * self.speed) + self.position.get_z())
        d = self.position.distance(next_position)
        for motion_source in self.get_all_motion_sources():
            energy_required += motion_source.get_energy_per_distance_unit() * d
        return energy_required * d <= self.current_energy

    def move(self):
        if self.speed <= 0 or not self.check_if_sufficient_energy(): return
        prev_location = self.position
        m = self.moves[self.direction]
        self.position = Coordinates((m[0] * self.speed) + prev_location.get_x(), (m[1] * self.speed)
        + prev_location.get_y(), (m[2] * self.speed) + prev_location.get_z())
        #print("PREV POS: {}, NEXT POS: {}".format(prev_location.get_coors(), self.position.get_coors()))
        #print(self.speed)
        #print(str((self.position.get_x(), self.position.get_y(), self.position.get_z())))
        self.register_energy_usage(prev_location)

    def update_position(self, position):
        self.position = Coordinates(position.x, position.y, position.z)

    def update_energy(self, energy):
        self.current_energy = energy

    def update_speed(self, speed):
        self.speed = speed

    def distance_from_mission_center(self, center):
        #print(str((self.position.get_x(), self.position.get_y(), self.position.get_z())))
        #print(str((center.get_x(), center.get_y(), center.get_z())))
        #return distance.euclidean((self.position.get_x(), self.position.get_y(), self.position.get_z()), (center.get_x(), center.get_y(), center.get_z()))
        #print(int(math.sqrt((self.position.get_x()-center.get_x())**2 + (self.position.get_y()-center.get_y())**2 + (self.position.get_z()-center.get_z())**2)))
        return int(math.sqrt((self.position.get_x()-center.get_x())**2 + (self.position.get_y()-center.get_y())**2 + (self.position.get_z()-center.get_z())**2))
    
    def distance(self, coors):
        return int(math.sqrt((self.position.get_x()-coors.get_x())**2 + (self.position.get_y()-coors.get_y())**2 + (self.position.get_z()-coors.get_z())**2))

    def check_for_sufficient_energy(self):
        #d = area.radius - self.distance_from_mission_center(area.center)
        #return self.current_energy - d * self.speed**2
        ms = None
        for sc in self.subcomponents.values():
            if isinstance(sc, MotionSource):
                ms = sc
                break
        return self.current_energy - (self.distance(self.starting_position) * ms.energy_per_distance_unit) > 0
    
    def start(self):
        if self.current_energy > 0:
            self.speed = 3
    
    def stop(self):
        self.speed = 0