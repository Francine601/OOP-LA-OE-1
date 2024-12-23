class Sinigang:
    def __init__(self, meat, souring_agent, vegatables):
        self.__meat = meat
        self.souring_agent = souring_agent
        self.vegatables = vegatables
       
    def __str__(self):
        return f"Sinigang with {self.__meat}, Souring agent: {self.souring_agent}, Vegatables: {self.vegatables}"
    def may_baboy_ba(self):
        return self.__meat
    def setter(self, new):
        self.__meat = new
sinigang_pork = Sinigang("Pork", "Tamarind", ["Kangkong", "Radish"])


sinigang_pork.setter("Liempo")
print(sinigang_pork.may_baboy_ba())