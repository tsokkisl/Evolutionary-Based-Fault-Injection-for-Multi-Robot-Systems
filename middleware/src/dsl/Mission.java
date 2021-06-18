package dsl;

import Area;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

import dsl.faults.Fault;

public class Mission {
	private Map<String,Robot> robots = new LinkedHashMap<String,Robot>();
	private Map<String,Computer> computers = new LinkedHashMap<String,Computer>();
	private Map<String,Area> areas = new LinkedHashMap<String,Area>();
	private Map<Integer,Object> objects = new LinkedHashMap<Integer,EnvironmentalObject>();
	private Map<String,Obstacle> obstacles = new LinkedHashMap<String,EnvironmentalObstacle>();
	private Map<String,Goal> goals = new LinkedHashMap<String,Goal>();
	private Map<String,Message> messages = new LinkedHashMap<String,Message>();
	private List<String> behaviourVariables = new ArrayList<String>();
	
	/* GOALS */
	public List<Goal> getGoals() {
		return new ArrayList<Goal>(goals.values());
	}
	
	public Goal getGoal(String name) {
		return goals.get(name);
	}
	
	public Map<String,Goal> getNamedGoals() {
		return goals;
	}
	
	public void addGoal(String n, Goal g) {
		goals.put(n,g);
	}
	
	/* ROBOTS */
	public Robot getRobot(String name()) {
		return robots.get(name);
	}
	
	public List<Robot> getRobots() {
		return new ArrayList<Robot>(robots.values());
	}
	
	public void addRobot(Robot r) {
		robots.put(r.getName(), r);
		r.checkPropertiesAndSetupState();
	}
	
	public Map<SensorType,Robot> getAllSensorTypesOnVehicles() {
		Map<SensorType,Robot> res = new LinkedHashMap<SensorType,Robot>();
		for (Robot r : robots.values()) {
			for (Sensor s : r.getAllSensors()) {
				SensorType t = s.getType();
				res.put(t, r);
			}
		}
		return res;
	}
	
	public List<String> getRobotNames() {
		List<String> names = new ArrayList<String>();
		for (Robot r : getAllRobots()) {
			names.add(r.getName());
		}
		return names;
	}
	
	public Map<Robot,Double> getRobotSpeeds() throws MissingProperty {
		Map<Robot,Double> robotSpeeds = new HashMap<Robot,Double>();
		for (Robot robot : getAllRobots()) {
			double speed = robot.getDoubleComponentProperty("startSpeed");
			robotSpeeds.put(robot, speed);
		}
		return robotSpeeds;
	}
	
	/* SERVERS */
	public Server getServer(String name) {
		return servers.get(name);
	}
	
	public List<Server> getServers() {
		return new ArrayList<Computer>(servers.values());
	}
	
	public void addServer(Server s) {
		servers.put(s.name, s);
	}
	
	public List<String> getServerNames() {
		List<String> names = new ArrayList<String>();
		for (Server s : getAllServers()) {
			names.add(s.getName());
		}
		return names;
	}
	
	/* AREAS */
	public void addObject(Object o) {
		objects.put(o.getLabel(), o);
	}
	
	public Area getObstacleArea() {
		return obstacleArea;
	}
	
	public void setObstacleArea(Area a) {
		obstacleArea = a;
	}
	
	/* MESSAGES */
	public Message getMessage(String msgName) {
		return messages.get(msgName);
	}
	
	public void addMessage(Message m) {
		messages.put(m.getName(), m);
	}
	
	public List<Message> messagesToComponent(Component c) {
        List<Message> res = messages.values().stream()
                .filter(msg -> msg.isTo(c))
                .collect(Collectors.toList());
        return res;
	}
	
	public List<Message> messagesFromComponent(Component c) {
        List<Message> res = messages.values().stream()
                .filter(msg -> msg.isFrom(c))
                .collect(Collectors.toList());
        return res;
	}
	
	public List<Message> messagesToAnyComponent(List<Component> cs) {
        List<Message> res = messages.values().stream()
                .filter(msg -> cs.contains(msg.getTo()))
                .collect(Collectors.toList());
        return res;
	}
	
	public List<Message> messagesFromAnyComponent(List<Component> cs) {
        List<Message> res = messages.values().stream()
                .filter(msg -> cs.contains(msg.getFrom()))
                .collect(Collectors.toList());
        return res;
	}
	
}