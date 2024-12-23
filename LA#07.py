class Car:
    def __init__(self, brand, color):  
        self.brand = brand
        self.color = color

car1 = Car("Ford", "Green")
print(f"Car 1 - Brand: {car1.brand}, Color: {car1.color}")

car1.color = "Blue"
print(f"Car 1 - Updated Color: {car1.color}")

car2 = Car("Honda", "White")
print(f"Car 2 - Brand: {car2.brand}, Color: {car2.color}")

print(f"Car 1 - Brand: {car1.brand}, Color: {car1.color}")
print(f"Car 2 - Brand: {car2.brand}, Color: {car2.color}")