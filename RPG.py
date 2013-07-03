#Imports
import pygame
import re

#Constants
MOVEMENT = 3
FPS_MAX = 60
BG_COLOR = (255, 255, 255)
BLOCK_SIZE = 32

MEDIA_PATH = "data"
PLAYER_PATH = "/player"

GREEN = (100, 200, 0)
BLUE = (5, 120, 155)
GREY = (145, 145, 145)

#Load Images
tile_wall = pygame.image.load(MEDIA_PATH + '/tiles/wall.png')
tile_grass = pygame.image.load(MEDIA_PATH + '/tiles/grass.png')
tile_water = pygame.image.load(MEDIA_PATH + '/tiles/water.png')


#Map-Generator
def generate_map(image_map, game):
    for j in range(image_map.get_height()):
        for i in range(image_map.get_width()):

            pixel = image_map.get_at((i, j))

            if pixel == GREEN:
                t = Tile((i * BLOCK_SIZE), (j * BLOCK_SIZE), tile_grass, game)
            if pixel == GREY:
                t = Wall((i * BLOCK_SIZE), (j * BLOCK_SIZE), tile_wall, game)
            if pixel == BLUE:
                t = Wall((i * BLOCK_SIZE), (j * BLOCK_SIZE), tile_water, game)


#Player and NPC stats
class Stats:

    def __init__(self, max_hp, health, strength, level, xp):
        self.max_hp = max_hp
        self.health = health
        self.stregth = stregth
        self.level = level
        self.xp = xp


#Tile
class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)
        self.pos = [x, y]
        self.image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

        self.rect = image.get_rect()
        self.rect.topleft = self.pos

        self.add(game.tiles)

    def update(self):

        screen.blit(self.image, self.pos)


#Wall
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, image, game):

        pygame.sprite.Sprite.__init__(self)
        self.pos = [x, y]
        self.image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.add(game.walls)

    def update(self):

        screen.blit(self.image, self.pos)


#Player
class Player(pygame.sprite.Sprite):

    def __init__(self, *groups):

        super(Player, self).__init__(*groups)
        self.image_path = MEDIA_PATH + '/player'
        self.way = 'down'

        self.image = pygame.image.load(self.image_path +
                                       '/down/1.png')
        self.image = pygame.transform.scale(self.image,
                                            (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = pygame.rect.Rect((400, 300),
                                     (BLOCK_SIZE - 2, BLOCK_SIZE - 2))

        self.counter = 1

    def update_img(self, vector):

        if vector == self.way:
            self.counter += 1
        else:
            self.counter = 1
            self.way = vector
        path = self.image_path + '/' + self.way + '/' \
            + (str)(((int)(self.counter / 7) % 5) + 1) + '.png'
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,
                                            (BLOCK_SIZE, BLOCK_SIZE))

    def update(self, dt, game):

        last = self.rect.copy()

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.x -= MOVEMENT# * dt
            self.update_img('left')
        else:
            if key[pygame.K_RIGHT]:
                self.rect.x += MOVEMENT# * dt
                self.update_img('right')
        if key[pygame.K_UP]:
            self.rect.y -= MOVEMENT# * dt
            self.update_img('up')
        else:
            if key[pygame.K_DOWN]:
                self.rect.y += MOVEMENT# * dt
                self.update_img('down')

        #dt disabled due to unknown bug        

        for cell in pygame.sprite.spritecollide(self, game, False):
            self.rect = last
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Game(object):

    def __init__(self):

        sprites = pygame.sprite.Group()

        self.tiles = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.player = Player(sprites)

        self.running = True

    def main(self, screen):
        #Science starts right about here
        pygame.init()

        map_bmp = pygame.image.load(MEDIA_PATH + "/level/01.bmp")

        generate_map(map_bmp, self)

        clock = pygame.time.Clock()
        dt = clock.tick(10)

        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.walls.update()
            self.tiles.update()
            self.player.update(dt/1000., self.walls)
            pygame.display.update()

        pygame.quit()


#PLAY THA GAME
screen = pygame.display.set_mode((800, 600))
game = Game()
game.main(screen)
