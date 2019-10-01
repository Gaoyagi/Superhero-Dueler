import random

#Ability class
class Ability(object):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, int(self.max_damage))


#weapon Class
class Weapon(Ability): 
    def attack(self):
        return random.randint(int(self.max_damage) // 2, int(self.max_damage))


#Armor Class
class Armor(object):
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block) 


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

    #adds a new weapon object to heroes list of abilities
    #param: new weapon object
    #return none
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
    def defend(self):
        defense = 0
        for armor in self.armors:
            defense += armor.block()
        return defense

    #activates the defend method and then caluclates the total damage taken and subtracts it from your current health
    #params: incoming damage
    #return: none
    def take_damage(self, damage):
        taken_damage = damage - self.defend()   
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
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print(f"{self.name} and {opponent.name} had a draw")
            return
        while(self.current_health > 0 and opponent.current_health > 0):
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
        if self.current_health > 0:
            print(self.name + " beat " + opponent.name)
            self.add_kills(1)
            opponent.add_deaths(1)  
        else:
            print(opponent.name + " beat " + self.name)
            self.add_deaths(1)
            opponent.add_kills(1)
           
    def add_kills(self, num_kills):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths




#Team Class
class Team(object):
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.dead = []
        self.total_kills = 0
        self.total_deaths = 0
        self.alive = True

    def add_hero(self, name):
        self.heroes.append(name)

    def remove_hero(self, name):
        found = False
        for hero in self.heroes:
            if(hero.name == name):  
                self.dead.append(hero)
                self.heroes.remove(hero)   
                found = True    
        if not found:        
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    #has the two teams attack each other until one team "dies"
    #params: enemy team object
    #return none
    def attack(self, other_team):
        while len(self.heroes) != 0 and len(other_team.heroes) != 0:
            random.shuffle(self.heroes)
            random.shuffle(other_team.heroes)
            self.heroes[0].fight(other_team.heroes[0])
            if self.heroes[0].current_health <= 0:
                self.dead.append(self.heroes.pop(0))
            elif other_team.heroes[0].current_health <= 0:
                other_team.dead.append(other_team.heroes.pop(0))

    #goes through the team's list of dead, "revives" them and then readding them to the live hero list
    #params: health??
    #return: none 
    def revive_heroes(self, health=100):
        for i in range(len(self.dead)):
            self.dead[0].current_health = self.dead[0].starting_health
            self.heroes.append(self.dead[0])
            self.dead.remove(self.dead[0])

    def stats(self):
        for hero in self.heroes:
            self.total_kills+=hero.kills
            self.total_deaths+=hero.deaths
            hero.kills = 0
            hero.deaths = 0
        for hero in self.dead:
            self.total_kills+=hero.kills
            self.total_deaths+=hero.deaths
            hero.kills = 0
            hero.deaths = 0


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
        damage = self.validNum(damage)
        return Ability(name, damage)

    #creates new weapon object
    #paramater: none
    #return: new weapon object
    def create_weapon(self):
        name = input("What is the weapon called? ")
        damage = input("how much damage does it do? ")
        damage = self.validNum(damage)
        return Weapon(name, damage)

    #creates new armor object
    #paramater: none
    #return: new armor object
    def create_armor(self):
        name = input("What is the armor called? ")
        block = input("how much damage does it block? ")
        block = self.validNum(block)
        return Armor(name, block)
    
    #creates new hero object and then adds weapons, armor, and abilites to the hero at the users request
    #param: non
    #return: new hero object
    def create_hero(self):
        name = input("what is the name of the hero? ")
        health = input("how much health does this hero have? ")
        health = self.validNum(health)
        neo = Hero(name, health)
        while self.validAnswer("ability"):
            neo.add_ability(self.create_ability())
        while self.validAnswer("weapon"):
            neo.add_weapon(self.create_weapon())
        while self.validAnswer("armor"):
            neo.add_armor(self.create_armor())
        return neo
                
    #function meant to make sure the user input to add is a valid answer to yes no questions
    #parameter: w/e the user wants to add to the hero
    #return: True or False depending if the user wants to continue adding
    def validAnswer(self, item):
        yes_no = True
        valid = False
        while not valid:
            response = input(f"would you like to add a(n) {item}? (y/n): ")
            response.lower()
            if response == "n":
                yes_no = False
                valid = True
            elif response == "y":
                yes_no = True
                valid = True
            else:
                print("Invalid choice")
        return yes_no

    def validNum(self, ans):
        invalid = True
        while invalid:
            try:
                ans = int(ans)
            except:
                ans = input("please enter a valid number: ")  
            else:
                invalid = False
        return ans
    
    def build_team_one(self):
        name = input("what would you like to name team 1? ")
        self.team_one = Team(name)
        mates = input("how many team members do you want? ")
        mates = self.validNum(mates)
        for x in range(mates):
            self.team_one.heroes.append(self.create_hero())
    
    def build_team_two(self):
        name = input("what would you like to name team 2? ")
        self.team_two = Team(name)
        mates = input("how many team members do you want? ")
        mates = self.validNum(mates)
        for x in range(mates):
            self.team_two.heroes.append(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)
    
    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()
        if(len(self.team_two.heroes) == 0):
            print(f"the winner is team {self.team_one.name}!")
            print("the survivors are: ")
            for hero in self.team_one.heroes:
                print(hero.name)
        else:
            print(f"the winner is team {self.team_two.name}!")
            print("the survivors are: ")
            for hero in self.team_two.heroes:
                print(hero.name)

        print(f"team one's avg K/D is: {self.team_one.total_kills}/{self.team_one.total_deaths}")
        print(f"team two's avg K/D is: {self.team_two.total_kills}/{self.team_two.total_deaths}")    
       


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()  
        
    