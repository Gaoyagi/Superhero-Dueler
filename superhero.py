import random

#hero class
class Hero(object):
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    #adds a new ability to a heros list of abilities
    #params: ability object
    #return: none
    def add_ability(self, ability):
        self.abilities.append(ability)

    #adds armor to armor list
    #params: new armor object
    #return: none
    def add_armor(self, armor):
        self.armors.append(armor)

    #activates all your abilities and tallies up the damage
    #params: none
    #return: total attack value
    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    #activates all armors and tallies up defense
    #params:none
    #return: total defense
    def defend(self, incoming_damage):
        defense = 0
        for armor in self.armors:
            defense += armor.block()
        return defense

    #activates the defend method and then caluclates the total damage taken and subtracts it from your current health
    #params: incoming damage
    #return: none
    def take_damage(self, damage):
        taken_damage = damage - self.defend(damage)
        self.current_health -= taken_damage
    
    #checks to see if your health is 0
    #params: none
    #return: True for alive, False for dead
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    #fight the opponent hero until one hero falls
    #param: opponent hero object
    #return: none
    def fight(self, opponent):
        while(self.current_health>0 and opponent.current_health>0):
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
        if self.current_health > 0:
            print(self.name + " won!")
        else:
            print(opponent.name + " won!")


#Ability class
class Ability(object):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


#weapon Class
class Weapon(Ability): 
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
    def attack(self):
        return random.randint(0, self.max_damage/2)


#Armor Class
class Armor(object):
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block) 


#Team Class
class Team(object):
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def add_hero(self, name):
        self.heroes.append(name)

    def remove_hero(self, name):
        try:
            self.heroes.remove(name)
        except:
            return 0
    def view_all_heroes(self):
        allHero = ", ".join(self.heroes)
        print(allHero)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)