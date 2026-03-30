

from pawpal_system import Pet, Feeding


def test_mark_complete_changes_status():
    feeding = Feeding("Steak", "7:00 AM", 2)
    assert feeding.completed == False, f"Expected completed to be False, got {feeding.completed}"
    feeding.mark_complete()
    assert feeding.completed == True, f"Expected completed to be True after mark_complete(), got {feeding.completed}"


def test_add_activity_increases_count():
    pet = Pet("Bulu", "Dog")
    assert len(pet.activities) == 0, f"Expected 0 activities, got {len(pet.activities)}"
    pet.add_activity(Feeding("Steak", "7:00 AM", 2))
    assert len(pet.activities) == 1, f"Expected 1 activity after adding, got {len(pet.activities)}"
