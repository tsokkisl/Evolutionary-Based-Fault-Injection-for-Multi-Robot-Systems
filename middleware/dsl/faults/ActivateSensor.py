class ActivateSensor:

    def __init__(self, sensor):
        self.sensor = sensor

    def run(self, mission):
        self.sensor.stop()