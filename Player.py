import Stats
import pygame
import constants
from constants import MEDIA_PATH, BLOCK_SIZE, MOVEMENT


# Player
class Player(pygame.sprite.Sprite):

    def __init__(self, position, game, stats=Stats.Stats(), *groups):

        super(Player, self).__init__(*groups)
        self.image_path = MEDIA_PATH + '/player'
        self.way = 'down'

        self.image = pygame.image.load(self.image_path +
                                       '/down/1.png')
        self.image = pygame.transform.scale(self.image,
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = pygame.rect.Rect(position,
                                     (BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        self.game = game
        self.counter = 1
        self.last = None
        self.stats = stats
        self.is_alive = True

    def update_img(self, vector):

        if vector == self.way:
            self.counter += 1
        else:
            self.counter = 1
            self.way = vector
        path = self.image_path + '/' + self.way + '/' \
            + (str)(((int)(self.counter / 7) % 5) + 1) + '.png'

        # type: /data/player/<viewing way>/<current animation>.png
        # 7 just looked like a nice constant for slowing down the animation

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,
                                            (BLOCK_SIZE, BLOCK_SIZE))

    def update(self, dt, game):

        self.last = self.rect.copy()

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.x -= MOVEMENT  # * dt
            self.update_img('left')
        else:
            if key[pygame.K_RIGHT]:
                self.rect.x += MOVEMENT  # * dt
                self.update_img('right')
        if key[pygame.K_UP]:
            self.rect.y -= MOVEMENT  # * dt
            self.update_img('up')
        else:
            if key[pygame.K_DOWN]:
                self.rect.y += MOVEMENT  # * dt
                self.update_img('down')

        # dt disabled due to unknown bug

        for cell in pygame.sprite.spritecollide(self, game, False):
            self.rect = self.last
        self.game.screen.blit(self.image, (self.rect.x, self.rect.y))
