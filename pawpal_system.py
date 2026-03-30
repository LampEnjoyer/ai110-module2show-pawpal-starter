class Activity:
    def __init__(self, priority: int):
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True


class Feeding(Activity):
    def __init__(self, food_type: str, time: str, priority: int):
        super().__init__(priority)
        self.food_type = food_type
        self.time = time


class Walk(Activity):
    def __init__(self, distance_miles: float, duration: int, time: str, priority: int):
        super().__init__(priority)
        self.distance_miles = distance_miles
        self.duration = duration
        self.time = time


class Medication(Activity):
    def __init__(self, name: str, dosage: str, frequency: str, priority: int):
        super().__init__(priority)
        self.name = name
        self.dosage = dosage
        self.frequency = frequency


class Appointment(Activity):
    def __init__(self, vet_name: str, reason: str, date: str, priority: int):
        super().__init__(priority)
        self.vet_name = vet_name
        self.reason = reason
        self.date = date


class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.activities: list[Activity] = []

    def add_activity(self, activity: Activity):
        self.activities.append(activity)


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.petlist: list[Pet] = []

    def add_pet(self, pet: Pet):
        self.petlist.append(pet)