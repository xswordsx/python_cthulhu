import pygame
from functions import *
from constants import *


class Game(object):

    def __init__(self):

        self.player_sprite = pygame.sprite.Group()

        self.tiles = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.player = None

        self.has_player = False
        self.running = False

    def main(self, screen):
        # Science starts right about here
        pygame.init()
        self.screen = screen
        map_bmp = pygame.image.load(MEDIA_PATH + "/level/01.bmp")

        generate_map(map_bmp, self)

        if self.has_player is True:
            self.running = True
        else:
            print(NO_PLAYER)

        clock = pygame.time.Clock()
        dt = clock.tick(30)
        dt = dt / 1000.
        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.walls.update()
            self.tiles.update()
            self.npc.update()
            self.player.update(dt, self.walls)
            for cell in pygame.sprite.spritecollide(self.player,
                                                    self.npc, False):
                if cell is True:
                    self.running = False
            #self.player.update(dt, self.npc)
            pygame.display.update()
        pygame.quit()
