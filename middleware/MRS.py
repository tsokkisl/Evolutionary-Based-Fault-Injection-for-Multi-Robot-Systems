from dsl.mission.Battery import Battery
from dsl.mission.Robot import Robot
from dsl.mission.Coordinates import Coordinates
from dsl.mission.Sensor import Sensor
from dsl.mission.MotionSource import MotionSource
import roslibpy
from threading import Thread

class MRS(Thread):
	
	robots = {}
	topics = {}
	flag = True
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.reset_robots()
	
	def reset_robots(self):	
		# Initilize Robot: TIM
		subcomponents = []
		# Initilize Robot: TIM's subcomponents
		sensor_s1 = Sensor("s1", "r1", "GPS_POSITION", 10.0, 20)
		subcomponents.append(sensor_s1)
		sensor_s2 = Sensor("s2", "r1", "PRESSURE", 22.0, 15)
		subcomponents.append(sensor_s2)
		motion_source_ms1 = MotionSource("ms1", 25.0)
		subcomponents.append(motion_source_ms1)
		battery_b1 = Battery("b1", 2000.0)
		subcomponents.append(battery_b1)
		battery_b2 = Battery("b2", 2000.0)
		subcomponents.append(battery_b2)
		robot_r1 = Robot("r1", "TIM", 10, Coordinates(2, 1, 1), subcomponents)
		robot_r1.configure_robot()
		self.robots["r1"] = robot_r1
		
		# Initilize Robot: JEN
		subcomponents = []
		# Initilize Robot: JEN's subcomponents
		sensor_s3 = Sensor("s3", "r2", "GPS_POSITION", 14.0, 40)
		subcomponents.append(sensor_s3)
		sensor_s4 = Sensor("s4", "r2", "TEMPERATURE", 20.0, 10)
		subcomponents.append(sensor_s4)
		motion_source_ms2 = MotionSource("ms2", 25.0)
		subcomponents.append(motion_source_ms2)
		battery_b3 = Battery("b3", 4000.0)
		subcomponents.append(battery_b3)
		battery_b4 = Battery("b4", 500.0)
		subcomponents.append(battery_b4)
		robot_r2 = Robot("r2", "JEN", 8, Coordinates(5, 2, 1), subcomponents)
		robot_r2.configure_robot()
		self.robots["r2"] = robot_r2
		
		# Initilize Robot: KAL
		subcomponents = []
		# Initilize Robot: KAL's subcomponents
		sensor_s5 = Sensor("s5", "r3", "GPS_POSITION", 22.0, 15)
		subcomponents.append(sensor_s5)
		sensor_s6 = Sensor("s6", "r3", "DEPTH", 15.0, 15)
		subcomponents.append(sensor_s6)
		motion_source_ms3 = MotionSource("ms3", 19.0)
		subcomponents.append(motion_source_ms3)
		battery_b5 = Battery("b5", 3000.0)
		subcomponents.append(battery_b5)
		battery_b6 = Battery("b6", 1000.0)
		subcomponents.append(battery_b6)
		robot_r3 = Robot("r3", "KAL", 5, Coordinates(8, 9, 2), subcomponents)
		robot_r3.configure_robot()
		self.robots["r3"] = robot_r3
		
	
	def run(self):
		self.client = roslibpy.Ros(host='localhost', port=9090)
		self.client.run()
					
		#--------------------------------- Robot TIM Topics ---------------------------------#
		r1_POSITION = roslibpy.Topic(self.client, '/r1_POSITION', 'std_msgs/String')
		self.topics["r1_POSITION"] = r1_POSITION
		r1_SPEED = roslibpy.Topic(self.client, '/r1_SPEED', 'std_msgs/String')
		self.topics["r1_SPEED"] = r1_SPEED
		r1_ENERGY = roslibpy.Topic(self.client, '/r1_ENERGY', 'std_msgs/String')
		self.topics["r1_ENERGY"] = r1_ENERGY
		s1_GPS_POSITION = roslibpy.Topic(self.client, '/s1_GPS_POSITION', 'std_msgs/String')
		self.topics["s1_GPS_POSITION"] = s1_GPS_POSITION
		s2_PRESSURE = roslibpy.Topic(self.client, '/s2_PRESSURE', 'std_msgs/String')
		self.topics["s2_PRESSURE"] = s2_PRESSURE
					
		#--------------------------------- Robot JEN Topics ---------------------------------#
		r2_POSITION = roslibpy.Topic(self.client, '/r2_POSITION', 'std_msgs/String')
		self.topics["r2_POSITION"] = r2_POSITION
		r2_SPEED = roslibpy.Topic(self.client, '/r2_SPEED', 'std_msgs/String')
		self.topics["r2_SPEED"] = r2_SPEED
		r2_ENERGY = roslibpy.Topic(self.client, '/r2_ENERGY', 'std_msgs/String')
		self.topics["r2_ENERGY"] = r2_ENERGY
		s3_GPS_POSITION = roslibpy.Topic(self.client, '/s3_GPS_POSITION', 'std_msgs/String')
		self.topics["s3_GPS_POSITION"] = s3_GPS_POSITION
		s4_TEMPERATURE = roslibpy.Topic(self.client, '/s4_TEMPERATURE', 'std_msgs/String')
		self.topics["s4_TEMPERATURE"] = s4_TEMPERATURE
					
		#--------------------------------- Robot KAL Topics ---------------------------------#
		r3_POSITION = roslibpy.Topic(self.client, '/r3_POSITION', 'std_msgs/String')
		self.topics["r3_POSITION"] = r3_POSITION
		r3_SPEED = roslibpy.Topic(self.client, '/r3_SPEED', 'std_msgs/String')
		self.topics["r3_SPEED"] = r3_SPEED
		r3_ENERGY = roslibpy.Topic(self.client, '/r3_ENERGY', 'std_msgs/String')
		self.topics["r3_ENERGY"] = r3_ENERGY
		s5_GPS_POSITION = roslibpy.Topic(self.client, '/s5_GPS_POSITION', 'std_msgs/String')
		self.topics["s5_GPS_POSITION"] = s5_GPS_POSITION
		s6_DEPTH = roslibpy.Topic(self.client, '/s6_DEPTH', 'std_msgs/String')
		self.topics["s6_DEPTH"] = s6_DEPTH
	

		while self.client.is_connected:
			for robot in self.robots.values():
				robot.move()
			#--------------------------------- Publish data of Robot TIM ---------------------------------#
			r1_POSITION.publish(roslibpy.Message({'data': str(self.robots["r1"].position.x) + ',' + str(self.robots["r1"].position.y) + ',' + 
			str(self.robots["r1"].position.z)}))
			r1_SPEED.publish(roslibpy.Message({'data': str(self.robots["r1"].speed)}))
			r1_ENERGY.publish(roslibpy.Message({'data': str(self.robots["r1"].current_energy)}))
	
			s1_GPS_POSITION.publish(roslibpy.Message({'data': str(self.robots["r1"].subcomponents["s1"].generate_samples())}))
	
			s2_PRESSURE.publish(roslibpy.Message({'data': str(self.robots["r1"].subcomponents["s2"].generate_samples())}))
		
			#--------------------------------- Publish data of Robot JEN ---------------------------------#
			r2_POSITION.publish(roslibpy.Message({'data': str(self.robots["r2"].position.x) + ',' + str(self.robots["r2"].position.y) + ',' + 
			str(self.robots["r2"].position.z)}))
			r2_SPEED.publish(roslibpy.Message({'data': str(self.robots["r2"].speed)}))
			r2_ENERGY.publish(roslibpy.Message({'data': str(self.robots["r2"].current_energy)}))
	
			s3_GPS_POSITION.publish(roslibpy.Message({'data': str(self.robots["r2"].subcomponents["s3"].generate_samples())}))
	
			s4_TEMPERATURE.publish(roslibpy.Message({'data': str(self.robots["r2"].subcomponents["s4"].generate_samples())}))
		
			#--------------------------------- Publish data of Robot KAL ---------------------------------#
			r3_POSITION.publish(roslibpy.Message({'data': str(self.robots["r3"].position.x) + ',' + str(self.robots["r3"].position.y) + ',' + 
			str(self.robots["r3"].position.z)}))
			r3_SPEED.publish(roslibpy.Message({'data': str(self.robots["r3"].speed)}))
			r3_ENERGY.publish(roslibpy.Message({'data': str(self.robots["r3"].current_energy)}))
	
			s5_GPS_POSITION.publish(roslibpy.Message({'data': str(self.robots["r3"].subcomponents["s5"].generate_samples())}))
	
			s6_DEPTH.publish(roslibpy.Message({'data': str(self.robots["r3"].subcomponents["s6"].generate_samples())}))
		
				
		for topic in self.topics:
			topic.unadvertise()
			
	def stop(self):
		self.client.terminate()
	
	def reset(self):
		self.reset_robots()
	
	def kill(self):
		print("Thread 2 killed...")
		self.flag = False