class Activity:
    def __init__(self, priority: int):
        self.priority = priority


class Feeding(Activity):
    def __init__(self, food_type: str, amount: float, time: str, priority: int):
        super().__init__(priority)
        self.food_type = food_type
        self.amount = amount
        self.time = time


class Walk(Activity):
    def __init__(self, distance_miles: float, duration_min: int, time: str, priority: int):
        super().__init__(priority)
        self.distance_miles = distance_miles
        self.duration_min = duration_min
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
        self.feedings: list[Feeding] = []
        self.walks: list[Walk] = []
        self.medications: list[Medication] = []
        self.appointments: list[Appointment] = []

    def add_feeding(self, feeding: Feeding):
        self.feedings.append(feeding)

    def add_walk(self, walk: Walk):
        self.walks.append(walk)

    def add_medication(self, medication: Medication):
        self.medications.append(medication)

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.petlist: list[Pet] = []

    def add_pet(self, pet: Pet):
        self.petlist.append(pet)