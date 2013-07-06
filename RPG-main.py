# Imports
import pygame
import random
import re
import os
# Import .py files
# from constants import *
from Game import *
from NPC import *
from Player import *
from Stats import *
from Tile import *
from Wall import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

# PLAY THA GAME
game = Game('2.bmp', False)
game.main()
