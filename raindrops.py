#! Raindrops only file.

import pygame
import sys
from random import randint
from pygame.sprite import Group, Sprite


class Background(Sprite):
    def __init__(self, rd_set, screen):
        Sprite.__init__(self)
        self.rd_set = rd_set
        self.screen = screen
        self.image = pygame.image.load('r_files/1.bmp')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0, 0

    def blitme(self):
        """Прорисовывает пришеля и его текущее положение"""
        self.screen.blit(self.image, self.rect)


class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 490
        self.bg_color = (255, 255, 255)
        self.raindrop_speed_factor = 2
        self.raindrop_allowed = 100
        self.raindrop_drop_speed = 5


class Raindrop(Sprite):
    def __init__(self, rd_set, screen):
        super(Raindrop, self).__init__()
        self.screen = screen
        self.rd_set = rd_set
        self.image = pygame.image.load('r_files/raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = rd_set.raindrop_speed_factor

    def update(self):
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_events(rd_set, screen, raindrops):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_keydown_events(event, rd_set, screen, raindrops):
    if event.key == pygame.K_q:
        sys.exit()


def fire_bullet(rd_set, screen, raindrops):
    if len(raindrops) < rd_set.raindrop_allowed:
        new_drop = Raindrop(rd_set, screen)
        new_drop.x = randint(0, 600)
        new_drop.rect.x = new_drop.x
        new_drop.rect.y = 0
        raindrops.add(new_drop)


def update_screen(rd_set, screen, raindrops, Background):
    screen.fill(rd_set.bg_color)
    screen.blit(Background.image, Background.rect)
    Background.blitme()
    raindrops.draw(screen)
    pygame.display.flip()


def update_raindrops(rd_set, raindrops):
    raindrops.update()
    for drop in raindrops.copy():
        if drop.rect.bottom >= 490:
            drop.remove(raindrops)


def create_drops(rd_set, screen, raindrops):
    drop = Raindrop(rd_set, screen)
    for alien_number in range(3):
        if randint(0, 20) == 3:
            fire_bullet(rd_set, screen, raindrops)


def raindrops():
    pygame.init()
    rd_set = Settings()
    screen = pygame.display.set_mode((rd_set.screen_width,
                                      rd_set.screen_height))
    pygame.display.set_caption("Raindrops")
    BackGround = Background(rd_set, screen)
    BackGround.x = 0
    BackGround.y = 0
    BackGround.blitme()
    raindrops = Group()
    while True:
        check_events(rd_set, screen, raindrops)
        create_drops(rd_set, screen, raindrops)
        update_raindrops(rd_set, raindrops)
        update_screen(rd_set, screen, raindrops, BackGround)


raindrops()
