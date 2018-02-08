#! Raindrops falling down with the village house screen program.

import pygame
import sys
from random import randint
from pygame.sprite import Group, Sprite


class Background(Sprite):
    """Class for background picture"""
    def __init__(self, rd_set, screen):
        Sprite.__init__(self)
        self.rd_set = rd_set
        self.screen = screen
        self.image = pygame.image.load('r_files/1.bmp')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0, 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Settings:
    """Class for settings of program"""
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 490
        self.bg_color = (255, 255, 255)
        self.raindrop_speed_factor = 2
        self.raindrop_allowed = 100
        self.raindrop_drop_speed = 5


class Raindrop(Sprite):
    """Class for raindrops falling down"""
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


def check_events():
    """Checking exit conditions"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def rainy_day(rd_set, screen, drops):
    """Create the rain, a lot of raindrops"""
    if len(drops) < rd_set.raindrop_allowed:
        new_drop = Raindrop(rd_set, screen)
        new_drop.x = randint(0, 600)
        new_drop.rect.x = new_drop.x
        new_drop.rect.y = 0
        drops.add(new_drop)


def update_screen(rd_set, screen, drops, background):
    """Updates screen"""
    screen.fill(rd_set.bg_color)
    screen.blit(background.image, background.rect)
    background.blitme()
    drops.draw(screen)
    pygame.display.flip()


def update_raindrops(drops):
    """Update raindrops and remove them if they reach the bottom"""
    drops.update()
    for drop in drops.copy():
        if drop.rect.bottom >= 490:
            drop.remove(drops)


def create_drops(rd_set, screen, drops):
    """Creates declared number of raindrops"""
    for drop_number in range(3):
        if randint(0, 20) == 3:
            rainy_day(rd_set, screen, drops)


def raindrops():
    """Start the rain!"""
    pygame.init()
    rd_set = Settings()
    screen = pygame.display.set_mode((rd_set.screen_width,
                                      rd_set.screen_height))
    pygame.display.set_caption("Raindrops")
    background = Background(rd_set, screen)
    background.x = 0
    background.y = 0
    background.blitme()
    drops = Group()
    while True:
        check_events()
        create_drops(rd_set, screen, drops)
        update_raindrops(drops)
        update_screen(rd_set, screen, drops, background)


raindrops()
