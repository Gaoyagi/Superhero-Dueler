from animal import Animal
class Dog(Animal):
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def woof(self):
        print("woof")

