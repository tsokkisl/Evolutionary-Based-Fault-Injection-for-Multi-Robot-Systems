package dsl.dslloader;

import dsl.*;
import dsl.faults.*;
import java.util.Optional;
import java.util.List;
import java.util.ArrayList;

public class FaultEngine {
	private Mission mission;
		
	public FaultEngine(Mission m) {
		this.mission = m;
	}
	
		
		MotionLoss ft = new MotionLoss(Robot1, 5) 
		Fault MotionFault = new Fault("MotionFault", ft, 2.0, 1.5);

		
		EnergyLoss ft = new EnergyLoss(Robot2, 500) 
		Fault EnergyLoss = new Fault("EnergyLoss", ft, 4.5, 3.0);

		
		DisableComponent ft = new DisableComponent(A2) 
		Fault DisableComponent = new Fault("DisableComponent", ft, 8.0, 5.0);

	 
}