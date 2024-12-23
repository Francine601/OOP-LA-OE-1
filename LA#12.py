class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def display_details(self):
        print(f"Toy name: {self.name}, Toy price: ${self.price}")
   
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

my_car = Car("Race Car", 29.99)
my_car.display_details()
