import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface(SIZE['paddle'], flags=pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLORS['paddle'], pygame.FRect((0, 0), SIZE['paddle']), 0, 5)

        self.rect = self.image.get_frect(center=POS['player'])

        self.direction = 0

    def move(self, delta_time):
        self.rect.centery += self.direction * SPEED['player'] * delta_time
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    def update(self, delta_time):
        self.get_direction()
        self.move(delta_time)