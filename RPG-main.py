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
screen = pygame.display.set_mode((800, 600))
game = Game()
game.main(screen)
