package dsl;

import java.util.List;
import java.util.Optional;

public class Coordinate {
	private double x;
	private double y;
	private double z;
	
	public Coordinate (double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Coordinate (double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	public double getX() {
		return x;
	}
	
	public double getY() {
		return y;
	}
	
	public double getZ() {
		return z;
	}
	
	public double distanceSqr(Coordinate c) {
		return Math.pow((c.x - this.x),2.0) + Math.pow((c.y - this.y), 2.0);
	}
	
	public double distance(Coordinate c) {
		return Math.sqrt(distanceSqr(c))
	}
	
	public Optional<Coordinate> findClosestPoint(List<Coordinate> coors) {
		Optional<Coordinate> closest = Optional.empty();
		double distance = Double.MAX_VALUE;
		for (Coordinate c : coors) {
			double d = distance(c);
			if (d < distance) {
				closest = Optional.of(c);
				distance = d;
			}
		}
		return closest;
	}
}