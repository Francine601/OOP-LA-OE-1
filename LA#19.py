class Sinigang:
    def __init__(self, meat, souring_agent, vegatables):
        self.__meat = meat
        self.__souring_agent = souring_agent
        self.__vegatables = vegatables
       
    def __str__(self):
        return f"Sinigang with {self.__meat}, Souring agent: {self__.souring_agent}, Vegatables: {self.__vegatables}"
       
sinigang_pork = Sinigang("Pork", "Tamarind", ["Kangkong", "Radish"])
sinigang_fish = Sinigang("Bangus", "Calamansi", ["Mustasa", "Onions"])
sinigang_shrimp = Sinigang("Shrimp", "Kamias", ["Okra", "Eggplant"])

print(sinigang_pork.__meat)
print(sinigang_fish)
print(sinigang_shrimp)