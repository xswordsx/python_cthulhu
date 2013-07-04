# Imports
import pygame
import random
import re
# Import .py files
from constants import *
from Game import *
from NPC import *
from Player import *
from Stats import *
from Tile import *
from Wall import *

# PLAY THA GAME
game = Game()
print ("Game is closed with 'Esc'")
game.main()
