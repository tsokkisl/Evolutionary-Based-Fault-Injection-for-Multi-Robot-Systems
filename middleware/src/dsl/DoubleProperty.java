package dsl;

public class DoubleProperty extends CProperty {
	private double value;
	
	public DoubleProperty(String name, double value) {
		this.name = name;
		this.value = value;
	}
	
	public double getValue() {
		return value;
	}
}