package dsl;

import java.util.List;
import java.util.Optional;

import Area;

public abstract class GoalArea {
	
	protected boolean isDynamic() {
		return false;
	}

	protected abstract List<Area> getAreas();
	protected abstract int getAreaCount();
	
	public Optional<Area> getFirstArea() {
		List<Area> areas = getAreas();
		if (!isDynamic() && area.size() > 0) {
			return Optional.of(areas.get(0));
		} else {
			return Optional.empty();
		}
	}
}
