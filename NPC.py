import pygame
import random
from constants import *


class NPC(pygame.sprite.Sprite):

    def __init__(self, x, y, stats, game):

        pygame.sprite.Sprite.__init__(self)

        self.pos = [x, y]
        self.counter = 0
        self.image = None  # Not sure if I should init it
        self.type = (random.randint(1, NPC_TYPES))
        self.image_path = MEDIA_PATH + '/npc/' + (str)(self.type) + '/'
        # self.image_path looks like: /data/npc/<monster type>/
        self.name = NPC_NAME[self.type]
        self.update_img()
        if stats is None:
            self.stats = Stats.Stats()
        else:
            self.stats = stats  # Make a copy of the object

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.game = game

        self.add(game.npc)

    def update_img(self):

        self.counter += 1
        self.image = pygame.image.load(self.image_path +
                                      (str)((int)(self.counter / 7) % 5)
                                       + '.gif')
        self.image = pygame.transform.scale(self.image,
                                            (BLOCK_SIZE, BLOCK_SIZE))

    def update(self):

        self.update_img()
        self.game.screen.blit(self.image, self.pos)
