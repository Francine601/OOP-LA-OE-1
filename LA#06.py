class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def laptop_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        
my_Laptop = Laptop("Asus", "Zephyrus G16 GA605")

my_Laptop.laptop_info()