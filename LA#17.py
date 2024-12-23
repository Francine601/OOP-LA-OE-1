class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
        
    def attack(self, target):
        if target.health <= 0:
            print(f"{target.health} has already been defeated!")
            return
        target.health -= self.atk_power
        print(f"{self.name} attacked {target.name} for {self.atk_power} damage!")
        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining")
        else:
            print(f"{target.name} has 0 health and has been defeated!")
           
    def heal(self, amount):
        if self.health > 0:
            self.health += amount
            print(f"{self.name} healed for {amount} health. Current health: {self.health}\n")
        else:
            print(f"{self.name} cannot heal because they are already defeated!")
           
ling = Player("Ling", 1000, 125)
lance = Player("Lance", 950, 135)

while ling.health > 0 and lance.health > 0:
    ling.attack(lance)
   
    if ling.health <= 0:
        print(f"{lance.name} wins!")
        break
ling.heal(10)
lance.heal(15)
