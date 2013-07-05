import pygame
import dumbmenu as menu

from constants import *

from Tile import Tile
from Wall import Wall
from NPC import NPC
from Player import Player


# Map-Generator
def generate_map(game):
    #Add walls to edge of screen
    for i in range(game.image_map.get_width() + 2):
        j = i * BLOCK_SIZE
        t = Wall(0, j, tile_wall, game)
        t = Wall((game.image_map.get_width() + 1) * BLOCK_SIZE,
                 j, tile_wall, game)

    for i in range(game.image_map.get_width()):
        j = (i + 1) * BLOCK_SIZE
        t = Wall(j, 0, tile_wall, game)
        t = Wall(j, (game.image_map.get_height() + 1) * BLOCK_SIZE,
                 tile_wall, game)
    #Generate insides of map
    for j in range(game.image_map.get_height()):
        for i in range(game.image_map.get_width()):

            pixel = game.image_map.get_at((i, j))
            pos = [((i + 1) * BLOCK_SIZE), ((j + 1) * BLOCK_SIZE)]

            if pixel == GREEN:
                t = Tile(pos[0], pos[1], tile_grass, game)

            elif pixel == GREY:
                t = Wall(pos[0], pos[1], tile_wall, game)

            elif pixel == BLUE:
                t = Wall(pos[0], pos[1], tile_water, game)

            elif pixel == BLACK:
                t = Tile(pos[0], pos[1], tile_grass, game)
                t = NPC(pos[0], pos[1], game)

            elif pixel == PLAYER:
                if game.has_player is False:
                    game.player = Player(pos, game, game.player_sprite)
                    game.has_player = True
                else:
                    print(SPAWN_POINT_EXISTS)

                t = Tile(pos[0], pos[1], tile_grass, game)
            else:
                t = Tile(pos[0], pos[1], tile_grass, game)


def npc_collide(game, prerender):

    text_bg = pygame.Surface((game.screen_size[0], TEXT_BG_HEIGHT))
    text_bg.fill(BG_COLOR)
    text_bg.set_alpha(BG_ALPHA)

    menu_list = ['Attack', 'Flee in Terror']
    # game.screen.blit(text_bg, (0, game.screen_size[1] - TEXT_BG_HEIGHT))

    if prerender is False:

        dm = menu.dumbmenu(game.screen, menu_list, 60,
                           game.screen_size[1] - TEXT_BG_HEIGHT,
                           'misc/coders_crux.ttf', 48, 2, BLACK, BLACK)
        if dm == 1 or dm == -1:
          # game.running = False  # Python-friendly
            game.player.rect = game.player.last
        game.update()  # Kills an annoying 'glitch' effect
