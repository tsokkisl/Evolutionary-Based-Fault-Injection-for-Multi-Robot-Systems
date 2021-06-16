package dsl;

import java.util.ArrayList;
import java.util.List;

public class GoalDependencies {
	private List<Goal> dependencies = new ArrayList<Goal>(); 
	double earliestStartTime;
	double latestFinishTime;
	
	public GoalDependencies(double earliestStartTime, double latestFinishTime) {
		this.earliestStartTime = earliestStartTime;
		this.latestFinishTime = latestFinishTime;
	}
	
	public void addDependency(Goal dependency) {
		dependencies.add(dependency);
	}
	
	public boolean isReady(double timeNow) {
		boolean depsReady = true;
		
		for (Goal d : dependencies) {
			if (!(d.isReady(timeNow)))
				depsReady = false;
		}
		return depsReady && (timeNow >= earliestStartTime) && (timeNow <= latestFinishTime); 
	}

	public boolean isLate(double timeNow) {
		return (timeNow > latestFinishTime);
	}

	public List<Goal> getDependencies() {
		return dependencies;
	}
}