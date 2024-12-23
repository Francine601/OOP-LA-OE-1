class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage! {target.name}'s health is now {target.health}.")

    def special_move(self):
        pass

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        print(f"{self.name} defends! {self.name}'s health is reduced by {reduced_damage} (new health: {self.health}).")

class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2 

class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def special_move(self):
        print(f"{self.name} casts Fireball!")
        self.attack(self)
        self.power = 100

class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")
        self.power = self.power * 2
        
class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50  

warrior = Warrior("Warrior", 150, 30)
mage = Mage("Mage", 120, 20)
archer = Archer("Archer", 100, 25)
monster = Monster("Monster", 300, 15)

warrior.attack(monster)
warrior.special_move()  
warrior.attack(monster)

mage.attack(monster)
mage.special_move()  
mage.attack(monster)

archer.attack(monster)
archer.special_move() 
archer.attack(monster)

monster.attack(warrior)
monster.special_move()  
monster.attack(warrior)

monster.attack(mage)
monster.special_move()  
monster.attack(mage)

monster.attack(archer)
monster.special_move() 
monster.attack(archer)

characters = [warrior, mage, archer, monster]
for character in characters:
    character.special_move()

