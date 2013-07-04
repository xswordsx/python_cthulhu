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

    def main(self):
        # Science starts right about here
        pygame.init()
        self.image_map = pygame.image.load(MEDIA_PATH + "/level/01.bmp")
        self.screen_size = self.image_map.get_size()
        self.screen_size = (self.screen_size[0] * BLOCK_SIZE,
                            self.screen_size[1] * BLOCK_SIZE)
        self.screen = pygame.display.set_mode(self.screen_size)

        generate_map(self)

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
                pass  # <-----Insert Collide-with-NPC commands here
            #self.player.update(dt, self.npc)
            pygame.display.update()
        pygame.quit()
