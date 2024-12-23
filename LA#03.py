class MobileLegendHero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe_hero(self):
        print(f"{self.name} is a {self.role} hero.")
        
hero = MobileLegendHero("Layla", "Marksman")

hero.describe_hero()
