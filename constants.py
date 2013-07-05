import pygame


# Constants
MOVEMENT = 3
FPS_MAX = 60
BG_COLOR = (255, 255, 255)
BLOCK_SIZE = 32
TEXT_BG_HEIGHT = 120
BG_ALPHA = 90

pygame.font.init()
BIT_FONT = pygame.font.Font('misc/coders_crux.ttf', 24)

MAX_LEVEL = 1
NPC_TYPES = 3

MEDIA_PATH = "data"
PLAYER_PATH = "/player"

# Map-generation color-code
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
