class Sinigang:
    def __init__(self, meat, souring_agent, vegetables):
        self.meat = meat
        self.souring_agent = souring_agent
        self.vegetables = vegetables

    def __str__(self):
        return f"Sinigang with {self.meat}, Souring agent: {self.souring_agent}, Vegetables: {self.vegetables} "
        
sinigang_pork = Sinigang("Pork", "Tamarind", ["Kangkong", "Radish", "Eggplant"])
sinigang_fish = Sinigang("Bangus", "Calamansi", ["Mustasa", "Onions", "Okra"])
sinigang_shrimp = Sinigang("Shrimp", "Kamias", ["String Beans", "Tomato", "Okra"])

print(sinigang_pork)
print(sinigang_fish)
print(sinigang_shrimp)
