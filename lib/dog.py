class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, breed):
        """Breed must be in the list of approved breeds"""
        APPROVED_BREEDS = ["Mastiff", "Beagle", "Poodle", "Labrador"]
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")
person.py

class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        """The job property"""
        return self._job

    @job.setter
    def job(self, job):
        """Job must be in the list of approved jobs"""
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            raise ValueError("Job must be in list of approved jobs.")