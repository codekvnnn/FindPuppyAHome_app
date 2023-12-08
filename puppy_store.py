from puppy import Puppy

class PuppyStore:
    def __init__(self):
        self.puppies = []

    def add_puppy(self, puppy):
        self.puppies.append(puppy)

    def list_puppies(self):
        return [str(puppy) for puppy in self.puppies if puppy.available]

    def adopt_puppy(self, name):
        for puppy in self.puppies:
            if puppy.name == name and puppy.available:
                puppy.available = False
                return f"{name} has been adopted!"
        return f"{name} is not available for adoption."
