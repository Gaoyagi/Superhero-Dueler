import random

#hero class
class Hero(object):
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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
            self.add_kills(1)
            opponent.add_deaths(1)
        else:
            print(opponent.name + " won!")
            self.add_deaths(1)
            opponent.add_kills(1)

    def add_kills(self, num_kills):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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
        self.max_damage = max_damage
        self.name = name

    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


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
        found = False
        for hero in self.heroes:
            if(hero.name == name):
                self.heroes.remove(hero)   
                found = True    
        if not found:        
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        random.shuffle(self.heroes)
        random.shuffle(other_team.heroes)
        teamCount = 0
        enemyCount = 0
        while(teamCount != len(self.heroes) and enemyCount != len(other_team.heroes)):
            self.heroes[teamCount].fight(other_team.heroes[enemyCount])
            if(self.heroes[teamCount].current_health == 0):
                teamCount+=1
            else:
                enemyCount+=1

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} has a K/D of {hero.kills}/{hero.deaths}")


#arena Class
class Arena(object):
    def _init__(self):
        self.team_one = None
        self.team_two = None

    #creates an abiluty object
    #parameter: none
    #return: new ability object
    def create_ability(self):
        name = input("What is the ability called? ")
        damage = input("how much damage does it do? ")
        return Ability(name, damage)

    #creates new weapon object
    #paramater: none
    #return: new weapon object
    def create_weapon(self):
        name = input("What is the weapon called? ")
        damage = input("how much damage does it do? ")
        return Weapon(name, damage)

    #creates new armor object
    #paramater: none
    #return: new armor object
    def create_armor(self):
        name = input("What is the armor called? ")
        block = input("how much damage does it block? ")
        return Armor(name, block)
    
    #creates new hero object and then adds weapons, armor, and abilites to the hero at the users request
    #param: non
    #return: new hero object
    def create_hero(self):
        name = input("what is the name of the hero? ")
        health = int(input("how much health does this hero have? "))
        neo = Hero(name, health)
        while self.validAnswer("ability"):
            neo.add_ability(self.create_ability())
        while self.validAnswer("weapon"):
            neo.add_weapon(self.create_weapon())
        while self.validAnswer("armor"):
            neo.add_armor(self.create_armor())
        return neo
                
    #function meant to make sure the user input to add is a valid answer
    #parameter: w/e the user wants to add to the hero
    #return: True or False depending if the user wants to continue adding
    def validAnswer(self, item):
        response = input(f"would you like to add a(n) {item}? (y/n): ")
        response.lower()
        yes_no = True
        valid = False
        while not valid:
            if response == "n":
                yes_no = False
                valid = True
            elif response == "y":
                yes_no = True
                valid = True
            else:
                print("Invalid choice")
        return yes_no
    
    def build_team_one(self):
        pass
    
    def build_team_two(self):
        pass


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