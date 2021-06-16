package dsl;

public class MotionSource extends SubComponent {
	private double energyPerDistance;
	
	public MotionSource(double energyPerDistance) {
		this.energyPerDistance = energyPerDistance;
	}
	
	public double getEnergyPerDistance() {
		return energyPerDistance;
	}
}
