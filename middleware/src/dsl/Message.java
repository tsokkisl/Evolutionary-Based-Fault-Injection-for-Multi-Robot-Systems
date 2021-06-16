package dsl;

import java.util.ArrayList;
import java.util.List;

public class Message {
	private String name;
	private List<Component> from = new ArrayList<Component>();
	private List<Component> to = new ArrayList<Component>();
	private double minFrequency;
	private double maxFrequency;
	private String head;
	private String body;
	
	public Message(String name) {
		this.name = name;
	}
	
	public Message(String name, Component fromSingle, Component toSingle) {
		this(name);
		this.from.add(fromSingle);
		this.to.add(toSingle);
	}
	
	public Message(String name, List<Component> fromMultiple, Component toSingle) {
		this(name);
		this.from.addAll(fromMultiple);
		this.to.add(toSingle);
	}
	
	public Message(String name, List<Component> fromMultiple, List<Component> toMultiple) {
		this(name);
		this.from.addAll(fromMultiple);
		this.to.addAll(toMultiple);
	}
	
	public Message(String name, Component fromSingle, List<Component> toMultiple) {
		this(name);
		this.from.add(fromSingle);
		this.to.addAll(toMultiple);
	}
	
	public boolean isTo(Component c) {
		return (this.to == c);
	}
	
	public boolean isFrom(Component c) {
		return (this.from == c);
	}
	
	public List<Component> getTo() {
		return to;
	}
	
	public List<Component> getFrom() {
		return from;
	}
	
	public String getName() {
		return name;
	}
}
