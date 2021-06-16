package atlasdsl;

import Coordinate;

public class Object extends Coordinate {
	private static int labelCounter = 1;
	
	private int label;
	private int width = 5;
	private boolean isHazard;
	private String color;
	
	public Object(Coordinate location, boolean isHazard) {
		super(location.getX(), location.getY());
		this.label = autoLabelCounter++;
		this.isHazard = isHazard;
		
		if (isHazard) {
			color = "red";
		} else {
			color = "green";
		}
	}
	
	public Object(int label, Coordinate location, boolean isHazard) {
		super(location.getX(), location.getY());
		this.label = label;
		this.isHazard = isHazard;
		
		if (isHazard) {
			color = "red";
		} else {
			color = "green";
		}
	}
	
	public int getLabel() {
		return label;
	}
}
