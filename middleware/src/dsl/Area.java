package dsl;

public class Area {
	private Coordinate c1;
	private Coordinate c2;
	
	public Area(double x1, double y1, double x2, double y2) {
		this.c1 = new Coordinate(x1, y1);
		this.c2 = new Coordinate(x2, y2);
	}
	
	public double width() {
		return Math.abs(c1.getX() - c2.getX());
	}

	public double height() {
		return Math.abs(c1.getY() - c2.getY());		
	}
	
	public double left() {
		return Math.min(c1.getX(), c2.getX());
	}
	
	public double bottom() {
		return Math.min(c1.getY(), c2.getY());
	}
	
	public double right() {
		return Math.max(c1.getX(), c2.getX());
	}
	
	public double top() {
		return Math.max(c1.getY(), c2.getY());
	}
	
	public boolean containsCoordinates(Coordinate c) {
		double x = c.getX();
		double y = c.getY();
		return (x > this.left() && x < this.right() && y > this.bottom() && y < this.top());
	}
}