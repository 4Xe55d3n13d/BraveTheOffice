import random

class Item():
    '''Base class for entities in the game, including the player and enemies
    
    Attributes:
        name (str): An Item's name.
        hp (int): An Item's current HP.
        hp_max (int): An Item's maximum HP.
        stats (dict of str:int): Dictionary that holds an item's stats.
    '''
    def __init__(self, name, atk, dfs, spd, hp):
        ''' Initialize the attributes of an Item object. '''
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.stats = {"atk": atk,
                        "dfs": dfs,
                        "spd": spd,}
    
    def attack(self, other):
        ''' Attacks an opponent in a combat encounter, reducing their HP.
        
        Args:
            other (item): the opponent in a combat encounter.
            
        Returns:
            damage (int): the amount of damage dealt to the opponent.
        '''
        if self.stats["dfs"] > other.stats["dfs"]:
            damage = random.randrange(1,4,1) + self.stats["spd"] + self.stats["atk"]
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
            
        if self.stats["dfs"] < other.stats["dfs"]:
            damage = random.randrange(1,4,1)
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
            
        if self.stats["dfs"] == other.stats["dfs"]:
            damage = random.randrange(1,4,1) + self.stats["atk"]
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
        
    def alive(self):
        ''' Returns if an item is dead (reduced to 0 HP) or not.

        Returns:
            bool: whether or not the item in question has an HP level greater than 0.
        '''
        return self.hp > 0
    
    def __str__(self):
        return f"Name: {self.name}\n Hit Points: {self.hp}\n Attack: {self.stats["atk"]}\n Defense: {self.stats["dfs"]}\n Speed: {self.stats["spd"]}"
    
    def __repr__(self):
        return f"Name: {self.name}\n Hit Points: {self.hp}\n Attack: {self.stats["atk"]}\n Defense: {self.stats["dfs"]}\n Speed: {self.stats["spd"]}"

class Player_Item(Item):
    '''Class for the Player entity.
    
    Attributes:
        name (str): An Item's name.
        hp (int): An Item's current HP.
        hp_max (int): An Item's maximum HP.
        stats (dict of str:int): Dictionary that holds an item's stats.
    '''
    def __init__(self, name, atk, dfs, spd, hp = 20):
        ''' Initialize the attributes of an playerItem object. '''
        super().__init__(name=name, atk=atk, dfs=dfs, spd=spd, hp = 70)
    
    def attack(self, other):
        ''' Attacks an opponent in a combat encounter, reducing their HP.
        Specific to a playerItem.
        
        Args:
            other (item): the opponent in a combat encounter.
            
        Returns:
            damage (int): the amount of damage dealt to the opponent.
        '''
        if self.stats["dfs"] > other.stats["dfs"]:
            damage = random.randrange(1,4,1) + self.stats["spd"] + self.stats["atk"] + 4
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
            
        if self.stats["dfs"] < other.stats["dfs"]:
            damage = random.randrange(1,4,1) + 4
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
            
        if self.stats["dfs"] == other.stats["dfs"]:
            damage = random.randrange(1,4,1) + self.stats["atk"] + 4
            other.hp -= damage
            other.hp = max(other.hp, 0)
            return damage
    
    def medkit_skill(self):
        ''' Restores a set amount of HP based on a skill check.
            
        Returns:
            healing (int): the amount of HP healed to the player by the skill.
        '''
        check = random.randrange(1,4,1) + self.stats["dfs"]
        healing = random.randrange(1,10,1) if check > 2 else 3
        self.hp += healing
        self.hp = max(self.hp, 0)
        return healing
    
    def distract_skill(self, other):
        ''' Lowers an enemy's DFS stat by 2 if their defense isn't already 2 or less.
        
        Args:
            other (item): the opponent in a combat encounter.
            
        Returns:
            other.stats["dfs"] (int): the enemy's defense stat.
        '''
        if other.stats["dfs"] > 2:
            other.stats["dfs"] -= 2
        return other.stats["dfs"]
    
    def flee_skill(self, other):
        ''' Performs a contested speed check where the item will flee a combat encounter if their SPD is greater.
        
        Args:
            other (item): the opponent in a combat encounter.
            
        Returns:
            bool: whether or not the current item has a SPD stat greater than or equal to another item's SPD stat.
        '''
        return True if self.stats["spd"] >= other.stats["spd"] else False

class Enemy_Item(Item):
    '''Class for enemy entities.
    
    Attributes:
        name (str): An Item's name.
        hp (int): An Item's current HP.
        hp_max (int): An Item's maximum HP.
        stats (dict of str:int): Dictionary that holds an item's stats.
        scenario (str): Unique combat scenario specific to an enemy.
    '''
    def __init__(self, name, atk, dfs, spd, scenario, hp):
        """ Initialize the attributes of an enemyItem object. """
        super().__init__(name=name, atk=atk, dfs=dfs, spd=spd, hp = hp)
        self.scenario = str(scenario)