class Vehicle:
    def __init__(self, brand, model, fueltype):
        self.brand = brand
        self.model = model
        self.fueltype = fueltype
    def describeVehicle(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel Type: {self.fueltype}")
   
class Car(Vehicle):
    pass

my_car = Car("Toyota","Corolla","Gasoline")
my_car.describeVehicle()

class Motorcycle(Vehicle):
    pass

my_motorcycle = Motorcycle("Yamaha","MT-07","Diesel")
my_motorcycle.describeVehicle()
    