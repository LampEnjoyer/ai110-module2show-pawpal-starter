from pawpal_system import Owner, Pet, Feeding, Walk, Medication

owner = Owner("Bob")

pet1 = Pet("Bulu", "Dog")
pet2 = Pet("Bill", "Cat")

owner.add_pet(pet1)
owner.add_pet(pet2)

pet1.add_activity(Feeding("Steak", "7:00 AM", 2))
pet1.add_activity(Walk(0.5, 20, "8:00 AM", 3))
pet1.add_activity(Medication("Heartguard", "1 chew", "monthly", 1))

pet2.add_activity(Feeding("Tuna", "7:30 AM", 2))
pet2.add_activity(Feeding("Tuna", "6:00 PM", 2))

print(f"=== Today's Schedule for {owner.name} ===\n")

for pet in owner.petlist:
    print(f"-- {pet.name} ({pet.species}) --")

    for activity in pet.activities:
        print(f"  {type(activity).__name__} (priority: {activity.priority})")

    print()