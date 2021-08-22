class DeactivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor

    def exec_fault(self, mission):
        self.sensor.stop()