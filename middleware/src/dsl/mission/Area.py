class Area :
	Coordinate c1;
	Coordinate c2;
	
	def Area(double: x1, double y1, double x2, double y2) {
		self.c1 = new Coordinate(x1, y1);
		self.c2 = new Coordinate(x2, y2);
	}
	
	def width(self):
		return Math.abs(c1.getX() - c2.getX());

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
		return (x > self.left() && x < self.right() && y > self.bottom() && y < self.top());
	}
}