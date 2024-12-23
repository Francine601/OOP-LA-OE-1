class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describePhones(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
       
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
       
my_phone = Android("Samsung", "A70")
my_phone.describePhones()