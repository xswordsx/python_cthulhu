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

        self.image_map = pygame.image.load(MEDIA_PATH + "/level/01.bmp")

        self.screen_size = self.image_map.get_size()
        self.screen_size = ((self.screen_size[0] + 2) * BLOCK_SIZE,
                            (self.screen_size[1] + 2) * BLOCK_SIZE)

        self.screen = pygame.display.set_mode(self.screen_size)
                                # Add pygame.NOFRAME to top statement
        self.screen.fill(BG_COLOR)

        generate_map(self)

    def update(self, dt=(pygame.time.Clock().tick(30) / 1000.)):

        self.walls.update()
        self.tiles.update()
        self.npc.update()
        self.player.update(dt, self.walls)
        for cell in pygame.sprite.spritecollide(self.player,
                                                self.npc, False):
            npc_collide(self)  # <-----Insert Collide-with-NPC commands here
        pygame.display.update()

    def loading_screen(self):
        img1 = pygame.image.load('misc/great_success.png')
        img1 = img1.convert()

        img2 = pygame.image.load('misc/title1.gif')
        img2 = img2.convert()

        img3 = pygame.image.load('misc/title2.gif')
        img3 = img3.convert()

        clock = pygame.time.Clock()
        tick_time = 20

        for i in range(40):
            clock.tick(tick_time)

            img1.set_alpha(i)

            self.screen.blit(img1, (190, -10))

            pygame.display.update()

        for i in range(100):
            clock.tick(tick_time)
            img1.set_alpha(i + 40)
            img2.set_alpha(i)

            self.screen.blit(img1, (190, -10))
            self.screen.blit(img2, (0, 490))

            pygame.display.update()

        self.screen.fill(BG_COLOR)

        for i in range(100):
            img3.set_alpha(i)

            self.screen.blit(img3, (0, 0))
            pygame.display.update()

            clock.tick(tick_time - 0.01)

        pygame.font.init()
        label = BIT_FONT.render('Press SPACE to continue...', 0, (0, 0, 0))
        self.screen.blit(label, (290, 580))
        pygame.display.update()

        flag = 0
        runny = True
        while runny:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    runny = False

                if event.type == pygame.KEYDOWN:
                    if event.unicode == " ":
                        flag = 1

            if flag:
                runny = False

    def main(self):
        # Science starts right about here
        pygame.init()

        if self.has_player is True:
            self.running = True
        else:
            print(NO_PLAYER)

        clock = pygame.time.Clock()
        dt = clock.tick(30)
        dt = dt / 1000.
        #Load some sweet, sweet credits
        #self.loading_screen()

        while self.running:
        # Main Loop
            clock.tick(60)
            # Quit events
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if key[pygame.K_ESCAPE]:
                    self.running = False

            self.update(dt)
        # End Main Loop
        pygame.quit()
