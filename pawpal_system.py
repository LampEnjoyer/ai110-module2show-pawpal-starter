PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def _parse_time(time_str: str) -> int:
    """Convert 'H:MM' or 'HH:MM' to minutes since midnight."""
    hours, minutes = time_str.split(":")
    return int(hours) * 60 + int(minutes)


class Activity:
    def __init__(self, name: str, duration: int, time: str, priority: str, recurrence: str = None):
        self.name = name
        self.duration = duration
        self.time = time
        self.priority = priority
        self.recurrence = recurrence  # None, "daily", "weekly"
        self.completed = False

    def start_minutes(self) -> int:
        return _parse_time(self.time)

    def end_minutes(self) -> int:
        return _parse_time(self.time) + self.duration

    def mark_complete(self):
        self.completed = True


class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.activities: list[Activity] = []

    def _conflicts(self, activity: Activity) -> list[Activity]:
        """Return existing activities whose time window overlaps with the given one."""
        new_start = activity.start_minutes()
        new_end = activity.end_minutes()
        return [
            a for a in self.activities
            if new_start < a.end_minutes() and a.start_minutes() < new_end
        ]

    def add_activity(self, activity: Activity) -> str:
        """
        Add an activity to the pet's schedule.

        - Recurring tasks: if a task with the same name and recurrence already
          exists, it is skipped instead of added as a duplicate.
        - Conflicts: if the new task overlaps in time with any existing task,
          it is rejected and the conflicting task names are returned.

        Returns a status string in all cases.
        """
        # Skip duplicate recurring tasks
        if activity.recurrence is not None:
            for a in self.activities:
                if a.name == activity.name and a.recurrence == activity.recurrence:
                    return f"Skipped: recurring '{activity.name}' ({activity.recurrence}) already scheduled."

        # Reject time conflicts
        overlapping = self._conflicts(activity)
        if overlapping:
            names = ", ".join(a.name for a in overlapping)
            return f"Conflict: '{activity.name}' at {activity.time} overlaps with: {names}."

        self.activities.append(activity)
        return f"Added: '{activity.name}' at {activity.time}."

    def sort_activity(self):
        """Sort activities by priority (high → medium → low), then by start time (earlier first)."""
        self.activities.sort(
            key=lambda a: (PRIORITY_ORDER.get(a.priority, 99), a.start_minutes())
        )


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.petlist: list[Pet] = []

    def add_pet(self, pet: Pet):
        self.petlist.append(pet)
