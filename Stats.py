import pygame


# Player and NPC stats
class Stats:

    def __init__(self, max_hp=65, strength=100, agility=100, level=1, xp=0):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.agility = agility
        self.level = level
        self.xp = xp
