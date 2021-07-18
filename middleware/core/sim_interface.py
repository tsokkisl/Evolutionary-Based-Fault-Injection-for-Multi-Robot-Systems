from ..src.dsl.mission import *
import time
import roslibpy

class SimInterface():
    
    topics = []

    def __init__(self):
        client = roslibpy.Ros(host='localhost', port=9090)
        client.run()
        #--------------------------------- Robot SAM Topics ---------------------------------#
        r1000_SPEED = roslibpy.Topic(client, '/r1000_SPEED', 'std_msgs/String')
        self.topics.add("r1000_SPEED", r1000_SPEED)
        r1000_ENERGY = roslibpy.Topic(client, '/r1000_ENERGY', 'std_msgs/String')
        self.topics.add("r1000_ENERGY", r1000_ENERGY)
        r1000_POSITION = roslibpy.Topic(client, '/r1000_POSITION', 'std_msgs/String')
        self.topics.add("r1000_POSITION", r1000_POSITION)
        s1000_GPS_POSITION = roslibpy.Topic(client, '/s1000_GPS_POSITION', 'std_msgs/String')
        self.topics.add("s1000_GPS_POSITION", s1000_GPS_POSITION)
        s1001_TEMPERATURE = roslibpy.Topic(client, '/s1001_TEMPERATURE', 'std_msgs/String')
        self.topics.add("s1001_TEMPERATURE", s1001_TEMPERATURE)
        
        #--------------------------------- Robot TOM Topics ---------------------------------#
        r1001_SPEED = roslibpy.Topic(client, '/r1001_SPEED', 'std_msgs/String')
        self.topics.add("r1001_SPEED", r1001_SPEED)
        r1001_ENERGY = roslibpy.Topic(client, '/r1001_ENERGY', 'std_msgs/String')
        self.topics.add("r1001_ENERGY", r1001_ENERGY)
        r1001_POSITION = roslibpy.Topic(client, '/r1001_POSITION', 'std_msgs/String')
        self.topics.add("r1001_POSITION", r1001_POSITION)
        s1002_PRESSURE = roslibpy.Topic(client, '/s1002_PRESSURE', 'std_msgs/String')
        self.topics.add("s1002_PRESSURE", s1002_PRESSURE)
        s1003_GPS_POSITION = roslibpy.Topic(client, '/s1003_GPS_POSITION', 'std_msgs/String')
        self.topics.add("s1003_GPS_POSITION", s1003_GPS_POSITION)
        
            

    def find_topic(self, obj, val):
        return self.topics.get(obj.ID + "_" + val)

    def get_sensor_sample(self, sensor):
        topic = self.find_topic(sensor.ID, sensor.sensorType)
        sample = topic.subscribe(lambda message: message['data'])
        return sample

    def get_POSITION(self, robot):
        topic = self.find_topic(robot.ID, "POSITION")
        position = topic.subscribe(lambda message: message['data'])
        return position
    
    def get_SPEED(self, robot):
        topic = self.find_topic(robot.ID, "SPEED")
        sample = topic.subscribe(lambda message: message['data'])
        return sample
        
    def get_ENERGY(self, robot):
        topic = self.find_topic(robot.ID, "ENERGY")
        sample = topic.subscribe(lambda message: message['data'])
        return sample
        

    def update_robot_speed(self, robot, new_speed):
        pass

            