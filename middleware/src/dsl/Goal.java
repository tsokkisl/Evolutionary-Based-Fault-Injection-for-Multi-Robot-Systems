package dsl;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Goal {
	private String name;
	private GoalDependencies dependecies;
	private GoalMembers members;
	private Optional<Area> goalArea;
	private GoalTask goalTask;
	
	public enum GoalStatus {
		PENDING,
		STARTED,
		COMPLETED,
		VIOLATED,
		MISSED
	}
	
	private GoalStatus status = GoalStatus.PENDING;
	
	public Goal(String name, GoalDependencies dependecies, GoalMembers members, Optional<Area> goalArea, GoalTask goalTask) {
		this.name = name;
		this.dependecies = dependecies;
		this.members = members;
		this.goalArea = goalArea;
		this.goalTask = goalTask;
	}
	
	public GoalStatus getStatus() {
		return status;
	}
	
	public String getName() {
		return name;
	}
	
	public void setStatus(GoalStatus gs) {
		status = gs;
	}
}