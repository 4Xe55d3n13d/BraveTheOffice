import random
import item
import csv
import copy
import sys

COMBAT_CONDITIONS = ("win", "loss", "fled")
SYNONYMS_FOR_ATTACK = ("Attack", "Politely debate them about TV shows", "Argue about salaries", "Staring contest", "Steel yourself", "Tell them to contact the General Manager")

class Game():
    '''Base class for the game.
    
    Attributes:
        rng (bool): Option to enable stat randomization for the player if True.
        challenge_mode (bool): Option to enable challenge mode if True.
        enemy_list (list of Enemy_Item): A list of all the possible enemies one can encounter in the game.
        map (list of Enemy_Item): The game map, populated with enemies selected at rando from enemy_list.
        hero (Player_Item): The player character.
    '''
    def __init__(self, name, randomizer, challenge):
        """ Initialize the attributes of a Game object. Also populates the enemy_list and game map."""
        self.randomizer = randomizer
        self.challenge_mode = challenge
        self.enemy_list = list()
        self.map = list()
        self.hero = (item.Player_Item(name, random.randrange(1,6,1),random.randrange(1,6,1),random.randrange(1,6,1),30)) if randomizer else (item.Player_Item(name, 4,6,5,30))
        with open("enemies.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if self.challenge_mode == True:
                    name = row[0]
                    attack = int(row[1]) + 2
                    defense = int(row[2]) + 2
                    speed = int(row[3]) + 2
                    hitp = int(row[4])
                    scenario = str(row[5])
                    self.enemy_list.append(item.Enemy_Item(name,attack,defense,speed,scenario,hitp))
                else:
                    name = row[0]
                    attack = int(row[1])
                    defense = int(row[2])
                    speed = int(row[3])
                    hitp = int(row[4])
                    scenario = str(row[5])
                    self.enemy_list.append(item.Enemy_Item(name,attack,defense,speed,scenario,hitp))
        for x in range(10):
            self.map.append(copy.deepcopy(self.enemy_list[random.randint(0,19)]))
    
    def start(self):
        """Begins the game."""
        print("You have to reach an elevator to get to your boss' office, but the walk is long and perilous. You must face ten trials to reach the elevator.\n")
        input("Press any key to begin.")
        print("Here is your character's stats.\n")
        print(self.hero.__str__())
        input("Press any key to continue.")
        
    def combat(self, adversary):
        """Begins a combat loop.
        
        Args:
            adversary (Enemy_Item): the opponent in a combat encounter.
            
        Returns:
            (str): string indicating the result of a combat round, either "win", "loss", or "fled."
        """
        while self.hero.alive():
            print(f"{adversary.scenario}")
            choice = str(input(f"What will you do?\nYou have {self.hero.hp} health.\n1. {SYNONYMS_FOR_ATTACK[random.randrange(0,5,1)]}\n2. Use a skill\n"))
            if choice == "1":
                print(f"\nYou dealt {self.hero.attack(adversary)} damage to {adversary.name}\n")
                print(f"{adversary.name} dealt {adversary.attack(self.hero)} damage to you.\n")
                if not self.hero.alive():
                    #loss condition
                    return COMBAT_CONDITIONS[1]
                elif not adversary.alive():
                    #win condition
                    return COMBAT_CONDITIONS[0]
            elif choice == "2":
                skill_choice = str(input(f"You can use the following skills.\n1. Flee\n2. Use A Distraction\n3. Use A Medkit\n"))
                if skill_choice == "1":
                    flee_result = self.hero.flee_skill(adversary)
                    if flee_result:
                        #flee condition
                        return COMBAT_CONDITIONS[2]
                    else:
                        print("\nYou couldn't flee the encounter\n")
                elif skill_choice == "2":
                    self.hero.distract_skill(adversary)
                    print("\nYou distracted your opponent.\n")
                elif skill_choice == "3":
                    heal_result = self.hero.medkit_skill()
                    print(f"\nYou healed {heal_result}.\n")
                else:
                    input("\nInvalid input.\nPress any key to continue.\n")
            else:
                input("\nInvalid input.\nPress any key to continue.\n")
    
    def game_over(self):
        """Ends the game."""
        print("You got to the elevator.\n") if self.hero.alive() else print("You died.\n")
        sys.exit()
                
    def play(self):
        """Allows the user to play the game through the terminal."""
        self.start()
        for tile in self.map:
            result = self.combat(tile)
            if result == "win":
                print("You won the encounter.\n")
                continue
            elif result == "loss":
                self.game_over()
            elif result == "fled":
                print("You fled the encounter.\n")
                continue
        self.game_over()
    
class Logging_Game(Game):
    '''Game class that includes logging functionality.
    
    Attributes:
        rng (bool): Whether or not the randomizer is enabled.
        challenge_mode (bool): Whether or not challenge mode is enabled.
        enemy_list (list of Enemy_Item): A list of all the possible enemies one can encounter in the game.
        map (list of Enemy_Item): The game map, populated with enemies selected at rando from enemy_list.
        hero (Player_Item): The player character.
        log (list of str): List of logs to be printed out in a text file.
    '''
    def __init__(self, name, rng, challenge):
        """Initialize the attributes of a Logging_Game object. Also populates the enemy_list, game map, and created the log list."""
        super().__init__(name, rng, challenge)
        self.log = list()
        
    def start(self):
        """Begins the game with added logging functionality."""
        super().start()
        self.log.append(f"Started Game.")
        self.log.append(f"{self.hero.__str__()}")
    
    def combat(self, adversary):
        """Begins a combat loop with added logging functionality.
        
        Args:
            adversary (Enemy_Item): the opponent in a combat encounter.
            
        Returns:
            (str): string indicating the result of a combat round, either "win", "loss", or "fled."
        """
        while self.hero.alive():
            print(f"{adversary.scenario}")
            self.log.append(f"{self.hero.name} got into an altercation with {adversary.name}")
            self.log.append(f"{adversary.__str__()}")
            choice = str(input(f"What will you do?\nYou have {self.hero.hp} health.\n1. {SYNONYMS_FOR_ATTACK[random.randrange(0,5,1)]}\n2. Use a skill\n"))
            if choice == "1":
                print(f"\nYou dealt {self.hero.attack(adversary)} damage to {adversary.name}\n")
                print(f"{adversary.name} dealt {adversary.attack(self.hero)} damage to you.\n")
                self.log.append(f"{self.hero.name} used the Attack skill.")
                if not self.hero.alive():
                    #loss condition
                    return COMBAT_CONDITIONS[1]
                elif not adversary.alive():
                    #win condition
                    return COMBAT_CONDITIONS[0]
            elif choice == "2":
                skill_choice = str(input(f"You can use the following skills.\n1. Flee\n2. Use A Distraction\n3. Use A Medkit\n"))
                if skill_choice == "1":
                    flee_result = self.hero.flee_skill(adversary)
                    if flee_result:
                        #flee condition
                        return COMBAT_CONDITIONS[2]
                    else:
                        print("\nYou couldn't flee the encounter\n")
                        self.log.append(f"{self.hero.name} couldn't flee the encounter.")
                elif skill_choice == "2":
                    self.hero.distract_skill(adversary)
                    print("\nYou distracted your opponent.\n")
                    self.log.append(f"{self.hero.name} used the Distract skill.")
                elif skill_choice == "3":
                    heal_result = self.hero.medkit_skill()
                    print(f"\nYou healed {heal_result}.\n")
                    self.log.append(f"{self.hero.name} used the Medkit skill.")
                else:
                    input("\nInvalid input.\nPress any key to continue.\n")
            else:
                input("\nInvalid input.\nPress any key to continue.\n")
            
    def game_over(self):
        """Ends the game and creates the log file."""
        print("Game ended. See gamelog.txt for result.\n")
        self.log.append(f"{self.hero.name} got to the elevator.") if self.hero.alive() else self.log.append(f"{self.hero.name} died.")
        with open('gamelog.txt', 'w') as file:
            for line in self.log:
                file.write(line + "\n")
            file.close()
                    
    def play(self):
        """Allows the user to play the game through the terminal with added logging functionality."""
        self.start()
        for tile in self.map:
            result = self.combat(tile)
            if result == "win":
                print("You won the encounter.\n")
                self.log.append(f"{self.hero.name} won the encounter.")
                continue
            elif result == "loss":
                break
            elif result == "fled":
                print("You fled the encounter.\n")
                self.log.append(f"{self.hero.name} fled the encounter.")
                continue
        self.game_over()