package atlasdsl;

import Coordinate;

public class Object extends Coordinate {
	private String type;
	private boolean isHazard;
	private String color;
	
	public Object(Coordinate location, boolean isHazard) {
		super(location.getX(), location.getY());
		this.type = "default";
		this.isHazard = isHazard;
		
		if (isHazard) {
			color = "red";
		} else {
			color = "green";
		}
	}
	
	public Object(String type, Coordinate location, boolean isHazard) {
		super(location.getX(), location.getY());
		this.type = type;
		this.isHazard = isHazard;
		
		if (isHazard) {
			color = "red";
		} else {
			color = "green";
		}
	}
	
	public int getType() {
		return type;
	}
}
