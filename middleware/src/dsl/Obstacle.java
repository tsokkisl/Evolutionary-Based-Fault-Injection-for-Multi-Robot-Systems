package dsl;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Obstacle {
	private List<Coordinate> polygon = new ArrayList<Coordinate>();
	private String label;
	
	public Obstacle(String label, List<Coordinate> polygon) {
		this.polygon = polygon;
		this.label = label;  
	}			
	
	public String getLabel() {
		return label;
	}
	
	public List<Coordinate> getCoordinates() {
		return polygon;
	}
}
