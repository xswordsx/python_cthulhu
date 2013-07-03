import pygame
import random
from constants import *


class NPC(pygame.sprite.Sprite):

    def __init__(self, x, y, game):

        pygame.sprite.Sprite.__init__(self)

        self.pos = [x, y]
        self.counter = 0
        self.image = None  # Not sure if I should init it
        self.image_path = MEDIA_PATH + '/npc/' + \
            (str)(random.randint(1, NPC_TYPES)) + '/'
        self.update_img()
        # self.image_path looks like: /data/npc/<monster type>/

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
