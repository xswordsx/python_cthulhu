import pygame

from constants import *

from Tile import Tile
from Wall import Wall
from NPC import NPC
from Player import Player


# Map-Generator
def generate_map(game):
    for j in range(game.image_map.get_height()):
        for i in range(game.image_map.get_width()):

            pixel = game.image_map.get_at((i, j))
            pos = [(i * BLOCK_SIZE), (j * BLOCK_SIZE)]

            if pixel == GREEN:
                t = Tile(pos[0], pos[1], tile_grass, game)

            if pixel == GREY:
                t = Wall(pos[0], pos[1], tile_wall, game)

            if pixel == BLUE:
                t = Wall(pos[0], pos[1], tile_water, game)

            if pixel == BLACK:
                t = Tile(pos[0], pos[1], tile_grass, game)
                t = NPC(pos[0], pos[1], game)

            if pixel == PLAYER:
                if game.has_player is False:
                    game.player = Player(pos, game, game.player_sprite)
                    game.has_player = True
                else:
                    print(SPAWN_POINT_EXISTS)

                t = Tile(pos[0], pos[1], tile_grass, game)
