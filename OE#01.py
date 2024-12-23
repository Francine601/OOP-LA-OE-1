class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} is a {self.role} with {self.damage_type} damage."

    def describe_hero(self):  
        print(f"{self.name} is a {self.role} hero with {self.damage_type} damage.")

    def describe_team(heroes):  
        print("Mobile Legends Lineup:")
        for hero in heroes:
            hero.describe_hero()
            
Exp = Hero("Chou", "Fighter", "Physical")
Jungler = Hero("Ling", "Assassin", "Physical")
Mid = Hero("Yve", "Mage", "Magical")
Roam = Hero("Tigreal", "Roam", "Physical")
Gold = Hero("Beatrix", "Marksman", "Physical")

Lineup = [Exp, Jungler, Mid, Roam, Gold]

Hero.describe_team(Lineup)
