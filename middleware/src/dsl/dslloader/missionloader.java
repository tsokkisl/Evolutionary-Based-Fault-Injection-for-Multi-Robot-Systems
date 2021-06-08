package dsl.dslloader;

import dsl.*;
import dsl.faults.*;
import java.util.Optional;
import java.util.List;
import java.util.ArrayList;

public class GeneratedDSLLoader implements DSLLoader {
	public Mission loadMission() throws DSLLoadFailed {
	
	Mission mission = new Mission();
	
	Server s1 = new Server("S1");
	mission.addServer(s1);
	
		Robot rR1 = new Robot("R1");
		rR1.setDoubleComponentProperty("d", 1000.0);
		rR1.setIntComponentProperty("i", 200);
		
 
			
			Actuator srR1_1 = new Actuator();
			rR1.addSubcomponent(srR1_1);
			
 
		Sensor srR1_2 = new Sensor(SensorType.SONAR);
		srR1_2.setParent(rR1);
		rR1.addSubcomponent(srR1_2);
			
			
 
			
			
 
			
			MotionSource srR1_4 = new MotionSource();
			rR1.addSubcomponent(srR1_4);
			
 
			
			
 
			
			
			
		mission.addRobot(rR1);
		Robot rR2 = new Robot("R2");
		
 
			
			Actuator srR2_1 = new Actuator();
			rR2.addSubcomponent(srR2_1);
			
 
			
			
 
			
			
 
			
			
 
			
			
 
			
			MotionSource srR2_6 = new MotionSource();
			rR2.addSubcomponent(srR2_6);
			
 
		Sensor srR2_7 = new Sensor(SensorType.CAMERA);
		srR2_7.setParent(rR2);
		rR2.addSubcomponent(srR2_7);
			
			
			
		mission.addRobot(rR2);
	
	
		
		
		GoalDependencies gd1 = new GoalDependencies(EolSequence [0.5], EolSequence [0.1]);
		
		
		
		
		GoalArea garG3 = new StaticGoalArea(
			new Area(new Point(0.0, 0.0, 0.0),
			           new Point(0.0, 0.0, 0.0)));
		
		
		Goal G3 = new Goal("G3", mission, gd1, gmG3, Optional.of(garG3), gt1);
		
		try {
			G3.setDependencyOn(EolSequence [G1, G2]);
		} catch (SelfDependencyError e) {
			throw new DSLLoadFailed("Goal G3 depends on itself");
		}
		
		mission.addGoal("G3", G3);
		
		
		GoalDependencies gd2 = new GoalDependencies(EolSequence [1.2], EolSequence [1.4]);
		
		
		
		
		
		GoalArea garG1 = new DynamicGoalArea(G3);
		
		Goal G1 = new Goal("G1", mission, gd2, gmG1, Optional.of(garG1), gt2);
		
		try {
			G1.setDependencyOn(EolSequence [G2]);
		} catch (SelfDependencyError e) {
			throw new DSLLoadFailed("Goal G1 depends on itself");
		}
		
		mission.addGoal("G1", G1);
		
		
		GoalDependencies gd3 = new GoalDependencies(EolSequence [2.0], EolSequence [4.0]);
		
		
		
		
		
		GoalArea garG2 = new DynamicGoalArea(G1);
		
		Goal G2 = new Goal("G2", mission, gd3, gmG2, Optional.of(garG2), gt3);
		
		try {
			G2.setDependencyOn(EolSequence []);
		} catch (SelfDependencyError e) {
			throw new DSLLoadFailed("Goal G2 depends on itself");
		}
		
		mission.addGoal("G2", G2);
	
 
		Message msgHeader of message = new Message("Header of message", Body of message, rR1, rR2);
		mission.addMessage(msgHeader of message); 
	
	return mission;
	}
}