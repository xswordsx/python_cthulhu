import pygame


# Constants
MOVEMENT = 3
FPS_MAX = 60
BG_COLOR = (255, 255, 255)
BLOCK_SIZE = 32
NPC_TYPES = 1

MEDIA_PATH = "data"
PLAYER_PATH = "/player"

GREEN = (100, 200, 0)
BLUE = (5, 120, 155)
GREY = (145, 145, 145)
BLACK = (0, 0, 0)
PLAYER = (255, 255, 255)

# Error Messages
SPAWN_POINT_EXISTS = "Game already has a player spawn point."
NO_PLAYER = "No player created."

# Load Images
tile_wall = pygame.image.load(MEDIA_PATH + '/tiles/wall.png')
tile_grass = pygame.image.load(MEDIA_PATH + '/tiles/grass.png')
tile_water = pygame.image.load(MEDIA_PATH + '/tiles/water.png')
