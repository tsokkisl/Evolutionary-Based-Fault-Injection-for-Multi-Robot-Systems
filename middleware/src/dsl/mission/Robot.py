from middleware.src.dsl.mission.SubComponent import SubComponent
from .Component import Component
from .Coordinate import Coordinate
from enum import Enum
from .Sensor import Sensor
from .MotionSource import MotionSource
from .Battery import Battery

class Robot(Component):
    name = ""
    subcomponents = {}
    currentEnergy = 0.0
    startingEnergy = 0.0

    class RobotType(Enum):
        TYPE_1 = 1,
        TYPE_2 = 2,
        TYPE_3 = 3

    type = RobotType.TYPE_1

    def __init__(self, name):
        self.name = name

    def addSubcomponent(self, id, subcomponent):
        self.subcomponents.put(id, subcomponent)
	
    def setInitialLocation(self):
        starting_location = self.getCoordinateComponentProperty("startLocation")
        self.setCoordinateComponentProperty("location", Coordinate(starting_location.getX(), starting_location.getY()))

    def configureRobot(self):
        try:
            self.setInitialLocation()
        except Exception:
            Exception.printStrackTrace()

    def getName(self):
        return self.name

    def getRobotType(self):
        return self.type
    
    def getSensorOfType(self, sensor_type):
        sensors = []
        for sc in self.subcomponents:
            if isinstance(sc, Sensor) and sc.sensorType == sensor_type:
                sensors.add(sc)
        return sensors

    def getAllSensors(self):
        sensors = []
        for sc in self.subcomponents:
            if isinstance(sc, Sensor):
                sensors.add(sc)
        return sensors

    def getMotionSource(self):
        for sc in self.subcomponents:
            if isinstance(sc, MotionSource):
                return sc

    def getAllBatteries(self):
        batteries = []
        for sc in self.subcomponents:
            if isinstance(sc, Battery):
                batteries.add(sc)
        return batteries

    def setupEnergyCapacity(self):
        for b in self.batteries:
            self.currentEnergy += b.getMaxEnergy()
            self.startingEnergy += b.getMaxEnergy()

    def getRemainingEnenergy(self):
        return self.currentEnergy

    def outOfEnergy(self):
        return self.currentEnergy <= 0.0

    def depleteEnergy(self, energy):
        self.currentEnergy -= energy

    def registerEnergyUsage(self, target_location):
        motion_source = self.getMotionSource()
        if motion_source != None:
            current_location = self.getCoordinateComponentProperty("location")
            d = current_location.distance(target_location)
            energy_required = motion_source.getEnergyPerDistance() * d
            self.currentEnergy -= energy_required
            self.currentEnergy = max(self.currentEnergy, 0.0)
        else:
            print("No motion source found!")