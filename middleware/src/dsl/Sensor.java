package dsl;

public class Sensor extends SubComponent {
	
	private enum SensorType {
		SONAR,
		GPS_POSITION,
		CAMERA;
	}
	
	private SensorType sensorType = sensorType.SONAR;
	
	public Sensor(SensorType sensor_type) {
		this.sensorType = sensor_type;
	}
	
	public SensorType getType() {
		return sensorType;
	}
	
	public static String sensorTypeToString(SensorType st) {
		return st.name();
	}
}