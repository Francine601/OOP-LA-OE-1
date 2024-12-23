class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
       
class Fish(Animal):
    def __init__(self, name, animal_type, can_swim=True):
        super().__init__(name, animal_type)
        self.can_swim = can_swim
       
my_fish = Fish(name = "Nemo", animal_type ="Clownfish", can_swim=True)
print(my_fish.can_swim)
