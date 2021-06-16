package dsl;

import java.util.ArrayList;
import java.util.List;

public class Server extends Component {
	private String name;
	private List<SubComponent> contains = new ArrayList<SubComponent>();
	
	public Server(String name) {
		this.name = name;
	}
	
	public String getName() {
		return name;
	}
}
