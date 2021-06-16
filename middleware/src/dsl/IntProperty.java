package dsl;

public class IntProperty extends CProperty {
	private int value;
	
	public IntProperty(String name, int value) {
		this.name = name;
		this.value = value;
	}
	
	public int getValue() {
		return value;
	}
}