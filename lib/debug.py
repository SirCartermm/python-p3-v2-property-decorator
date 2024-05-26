from dog import Dog
from person import Person

def test_dog_class():
    # Test 1: Create a Dog instance
    fido = Dog("Fido", "Mastiff")
    print("Test 1: Created a Dog instance")
    print("Name:", fido.name)
    print("Breed:", fido.breed)
    print()

    # Test 2: Set name and breed
    fido.name = "Buddy"
    fido.breed = "Beagle"
    print("Test 2: Set name and breed")
    print("Name:", fido.name)
    print("Breed:", fido.breed)
    print()

    # Test 3: Invalid name
    try:
        fido.name = "This is a very long name that exceeds 25 characters"
    except ValueError as e:
        print("Test 3: Invalid name (expected)")
        print(e)
    print()

    # Test 4: Invalid breed
    try:
        fido.breed = "Dragon"
    except ValueError as e:
        print("Test 4: Invalid breed (expected)")
        print(e)
    print()

def test_person_class():
    # Test 1: Create a Person instance
    person = Person("John Doe", "Admin")
    print("Test 1: Created a Person instance")
    print("Name:", person.name)
    print("Job:", person.job)
    print()

    # Test 2: Set name and job
    person.name = "Jane Doe"
    person.job = "Marketing"
    print("Test 2: Set name and job")
    print("Name:", person.name)
    print("Job:", person.job)
    print()

    # Test 3: Invalid name
    try:
        person.name = "This is a very long name that exceeds 25 characters"
    except ValueError as e:
        print("Test 3: Invalid name (expected)")
        print(e)
    print()

    # Test 4: Invalid job
    try:
        person.job = "Astronaut"
    except ValueError as e:
        print("Test 4: Invalid job (expected)")
        print(e)
    print()

if __name__ == "__main__":
    test_dog_class()
    test_person_class()