package dsl.dslloader;

import dsl.*;
import dsl.faults.*;
import java.util.Optional;
import java.util.List;
import java.util.ArrayList;

public class FaultScenario {
	private Mission mission;
		
	public FaultScenario(Mission m) {
		this.mission = m;
	}
	
	/* Fault Scenario 1 */
		
	DisableComponent ft = new DisableComponent(m.robots.get())
	Fault  = new Fault("", ft, 0.0, 0.0);

		
	Fault  = new Fault("", ft, 0.0, 0.0);

		
	MotionLoss ft = new MotionLoss(, 0) 
	Fault  = new Fault("", ft, 0.0, 0.0);

	 
	
	/* Fault Scenario 2 */
		
	Fault  = new Fault("", ft, 0.0, 0.0);

		
	Fault  = new Fault("", ft, 0.0, 0.0);

		
	EnergyLoss ft = new EnergyLoss(, 0) 
	Fault  = new Fault("", ft, 0.0, 0.0);

	 
}