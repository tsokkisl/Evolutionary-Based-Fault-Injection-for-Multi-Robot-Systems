package dsl;

public class StringProperty extends CProperty {
	private String value;

	public StringProperty(String name, String value) {
		this.name = name;
		this.value = value;
	}

	public String getValue() {
		return value;
	}
}