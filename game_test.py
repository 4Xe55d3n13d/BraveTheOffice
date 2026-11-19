import pytest
import item
import game
import random

def test_hero_creation():
    
    hero = item.Player_Item("Miriam", random.randrange(1,4,1),random.randrange(1,4,1),random.randrange(1,4,1),10)
    assert(hero.name is not None)
    assert(hero.attack is not None)
    assert(hero.stats["atk"] is not None)
    assert(hero.stats["dfs"] is not None)
    assert(hero.stats["spd"] is not None)
    assert(hero.hp == hero.hp_max)

def test_enemy_creation():
    villain = item.Enemy_Item("Fake Miriam", random.randrange(1,4,1),random.randrange(1,4,1),random.randrange(1,4,1),"You see a doppelganger of yourself.",30)
    assert(villain.name is not None)
    assert(villain.stats["atk"] is not None)
    assert(villain.stats["dfs"] is not None)
    assert(villain.stats["spd"] is not None)
    assert(villain.hp == villain.hp_max)
    assert(villain.scenario is not None)

def test_hero_creation_randomizer():
    game1 = game.Game("Miriam", True, False)
    hero = game1.hero
    assert(hero.name is not None)
    assert(hero.stats["atk"] is not None)
    assert(hero.stats["dfs"] is not None)
    assert(hero.stats["spd"] is not None)
    assert(hero.hp == hero.hp_max)
    
def test_hero_creation_non_randomizer():
    game1 = game.Game("Miriam", False, False)
    hero = game1.hero
    assert(hero.name is not None)
    assert(hero.stats["atk"] == 4)
    assert(hero.stats["dfs"] == 6)
    assert(hero.stats["spd"] == 5)
    assert(hero.hp == hero.hp_max)

def test_attack():
    hero = item.Player_Item("Miriam", 3,3,3,30)
    villain = item.Enemy_Item("Fake Miriam", 3,3,3,"You see a doppelganger of yourself.",30)
    villain.attack(hero)
    hero.attack(villain)
    assert(hero.hp < hero.hp_max)
    assert(villain.hp < villain.hp_max)

def test_distract():
    hero = item.Player_Item("Miriam", 3,3,3,30)
    villain = item.Enemy_Item("Fake Miriam", 3,2,3,"You see a doppelganger of yourself.",30)
    villain2 = item.Enemy_Item("Another Fake Miriam", 3,1,3,"You see a doppelganger of yourself.",30)
    villain3 = item.Enemy_Item("Yet Another Fake Miriam", 3,3,3,"You see a doppelganger of yourself.",30)
    hero.distract_skill(villain)
    hero.distract_skill(villain2)
    hero.distract_skill(villain3)
    assert villain.stats["dfs"] == 2
    assert villain2.stats["dfs"] == 1
    assert villain3.stats["dfs"] == 1

def test_medkit():
    hero = item.Player_Item("Miriam", 3,3,3,30)
    villain = item.Enemy_Item("Fake Miriam", 3,2,3,"You see a doppelganger of yourself.",30)
    villain.attack(hero)
    hurt = hero.hp
    healing_amount = hero.medkit_skill()
    assert healing_amount != 0
    assert hero.hp > hurt

def test_flee():
    hero = item.Player_Item("Miriam", 3,3,4,30)
    villain = item.Enemy_Item("Fake Miriam", 3,3,2,"You see a doppelganger of yourself.",30)
    hero2 = item.Player_Item("Miriam", 3,3,1,30)
    villain2 = item.Enemy_Item("Fake Miriam", 3,2,3,"You see a doppelganger of yourself.",30)
    assert hero.flee_skill(villain) == True
    assert hero2.flee_skill(villain2) == False
    
def test_log_game():
    gameyay = game.Logging_Game("Miriam", False, False)
    assert(gameyay.log is not None)