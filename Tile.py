import pygame
from constants import BLOCK_SIZE


# Tile
class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)
        self.pos = [x, y]
        self.image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

        self.rect = image.get_rect()
        self.rect.topleft = self.pos

        self.game = game

        self.add(game.tiles)

    def update(self):

        self.game.screen.blit(self.image, self.pos)
