package dsl.faults;

import java.util.Optional;

public class Fault {
	
	private String name;
	private double startTime;
	private double finishTime;
	private FaultType type;
	
	public Fault(String name, FaultType ft, double earliestStartTime, double latestStartTime) {
		this.name = name;
		this.type = ft;
		this.startTime = earliestStartTime;
		this.finishTime = latestFinishTime;
	}

	public String getName() {
		return name;
	}
	
	public double getEarliestStartTime() {
		return startTime;
	}
	
	public double getLatestEndTime() {
		return finishTime;
	}
}