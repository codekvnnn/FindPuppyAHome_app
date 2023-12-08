class Puppy:
    def __init__(self, name, breed, age, available=True):
        self.name = name
        self.breed = breed
        self.age = age
        self.available = available

    def __str__(self):
        return f"{self.name} - {self.breed}, Age: {self.age}, {'Available' if self.available else 'Not Available'}"
