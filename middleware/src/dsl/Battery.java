package dsl;

public class Battery extends EnergyResource {
	private int totalEnergy;
	private int currentEnergy;
	
	public Battery(int energy) {
		this.totalEnergy = energy;
	}
	
	public int getTotalEnergy() {
		return totalEnergy;
	}
	
	public boolean isEnergyDeplenished() {
		return currentEnergy == 0;
	}
	
	public void spendEnergy(int e) {
		currentEnergy -= e;
		if (currentEnergy < 0) {
			currentEnergy = 0;
		}
	}
	
	public double getRemainingEnergyPercentage() {
		return ((double)currentEnergy) / ((double)totalEnergy)
	}
}