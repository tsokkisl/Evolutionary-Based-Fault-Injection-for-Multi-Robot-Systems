from dsl.mission.Coordinates import Coordinates
import roslibpy
from threading import Thread
from gen.MRS import MRS
import time

class SimInterface(Thread):
    
    topics = {}
    mission = None
    flag = True
	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def MRS_init(self):
        # Setup MRS
        print("-------------------- Initilising and starting MRS --------------------\n")
        self.mrs = MRS()
        self.mrs.daemon = True
        self.mrs.start()
        
    def reset(self):
        #print("Thread 1 reset...")
        self.topics.clear()
     
    def kill(self):
    	print("Thread 1 killed...")
    	self.flag = False
                  
    def run(self):
    
        self.client = roslibpy.Ros(host='localhost', port=9090)
        self.client.run()
            
        #--------------------------------- Robot LEN Topics ---------------------------------#
        r1_POSITION = roslibpy.Topic(self.client, '/r1_POSITION', 'std_msgs/String')
        r1_POSITION.subscribe(lambda message: self.assign_to_topic('r1_POSITION', message))
        r1_SPEED = roslibpy.Topic(self.client, '/r1_SPEED', 'std_msgs/String')
        r1_SPEED.subscribe(lambda message: self.assign_to_topic('r1_SPEED', message))
        r1_ENERGY = roslibpy.Topic(self.client, '/r1_ENERGY', 'std_msgs/String')
        r1_ENERGY.subscribe(lambda message: self.assign_to_topic('r1_ENERGY', message))
        s1_GPS_POSITION = roslibpy.Topic(self.client, '/s1_GPS_POSITION', 'std_msgs/String')
        s1_GPS_POSITION.subscribe(lambda message: self.assign_to_topic('s1_GPS_POSITION', message))
        s2_PRESSURE = roslibpy.Topic(self.client, '/s2_PRESSURE', 'std_msgs/String')
        s2_PRESSURE.subscribe(lambda message: self.assign_to_topic('s2_PRESSURE', message))
            
        #--------------------------------- Robot JEN Topics ---------------------------------#
        r2_POSITION = roslibpy.Topic(self.client, '/r2_POSITION', 'std_msgs/String')
        r2_POSITION.subscribe(lambda message: self.assign_to_topic('r2_POSITION', message))
        r2_SPEED = roslibpy.Topic(self.client, '/r2_SPEED', 'std_msgs/String')
        r2_SPEED.subscribe(lambda message: self.assign_to_topic('r2_SPEED', message))
        r2_ENERGY = roslibpy.Topic(self.client, '/r2_ENERGY', 'std_msgs/String')
        r2_ENERGY.subscribe(lambda message: self.assign_to_topic('r2_ENERGY', message))
        s3_GPS_POSITION = roslibpy.Topic(self.client, '/s3_GPS_POSITION', 'std_msgs/String')
        s3_GPS_POSITION.subscribe(lambda message: self.assign_to_topic('s3_GPS_POSITION', message))
        s4_TEMPERATURE = roslibpy.Topic(self.client, '/s4_TEMPERATURE', 'std_msgs/String')
        s4_TEMPERATURE.subscribe(lambda message: self.assign_to_topic('s4_TEMPERATURE', message))
            
        #--------------------------------- Robot KAL Topics ---------------------------------#
        r3_POSITION = roslibpy.Topic(self.client, '/r3_POSITION', 'std_msgs/String')
        r3_POSITION.subscribe(lambda message: self.assign_to_topic('r3_POSITION', message))
        r3_SPEED = roslibpy.Topic(self.client, '/r3_SPEED', 'std_msgs/String')
        r3_SPEED.subscribe(lambda message: self.assign_to_topic('r3_SPEED', message))
        r3_ENERGY = roslibpy.Topic(self.client, '/r3_ENERGY', 'std_msgs/String')
        r3_ENERGY.subscribe(lambda message: self.assign_to_topic('r3_ENERGY', message))
        s5_GPS_POSITION = roslibpy.Topic(self.client, '/s5_GPS_POSITION', 'std_msgs/String')
        s5_GPS_POSITION.subscribe(lambda message: self.assign_to_topic('s5_GPS_POSITION', message))
        s6_DEPTH = roslibpy.Topic(self.client, '/s6_DEPTH', 'std_msgs/String')
        s6_DEPTH.subscribe(lambda message: self.assign_to_topic('s6_DEPTH', message))
        try:
            while self.flag:
                pass
        except KeyboardInterrupt:
            self.client.terminate()
            
    def assign_to_topic(self, topic_name, msg):
        self.topics[topic_name] = msg

    def get_sensor_sample(self, sensor):
        if sensor.ID + "_" + sensor.sensor_type in self.topics.keys():
            sample = self.topics[sensor.ID + "_" + sensor.sensor_type]["data"]
            return int(sample)
        else:
            return 0

    def get_POSITION(self, robot):
        if robot.ID + "_" + "POSITION" in self.topics.keys():
            position = self.topics[robot.ID + "_" + "POSITION"]["data"]
            position = position.split(',')
            return Coordinates(int(position[0]), int(position[1]), int(position[2]))
        else:
            return robot.position
    
    def get_SPEED(self, robot):
        if robot.ID + "_" + "SPEED" in self.topics.keys():
            position = self.topics[robot.ID + "_" + "SPEED"]["data"]
            return int(position)
        else:
            return robot.speed
        
    def get_ENERGY(self, robot):
        if robot.ID + "_" + "ENERGY" in self.topics.keys():
            energy = self.topics[robot.ID + "_" + "ENERGY"]["data"]
            return float(energy)
        else: 
            return robot.current_energy
        
    def update_robot_speed(self, robot, new_speed):
        self.mission.robots[robot.ID].speed = new_speed

    def stop(self):
        self.client.terminate()   