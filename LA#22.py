class BirthdayParty:
    def __init__(self, theme, foods):
        self.theme = theme
        self.foods = foods
    
    def print_foods(self):
        print(f"Theme: {self.theme}")
        print("Food at the party:")
        for food in self.foods:
            print(f"- {food}")
        self.__print_secret_dish()  
    
    def __print_secret_dish(self):
        print("Secret Dish: Birthday Cake")

party1 = BirthdayParty("Superhero", ["Pizza", "Hotdog", "Chips"])
party2 = BirthdayParty("Princess", ["Cupcakes", "Fruit Salad", "Ice Cream"])
party3 = BirthdayParty("Retro", ["Burgers", "Fries", "Milkshakes"])

print("Party 1:")
party1.print_foods()
print("\nParty 2:")
party2.print_foods()
print("\nParty 3:")
party3.print_foods()