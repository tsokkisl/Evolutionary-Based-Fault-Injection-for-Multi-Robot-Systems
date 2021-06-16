package dsl.faults;

import dsl.*;

public class ComponentFault extends FaultType {
	
	private Component affectedComponent;
	
	public ComponentFault(Component c) {
		this.affectedComponent = c;
	}
}