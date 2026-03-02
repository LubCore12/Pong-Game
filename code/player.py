import pygame

from settings import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface(SIZE['paddle'], flags=pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLORS['paddle'], pygame.FRect((0, 0), SIZE['paddle']), 0, 5)
        self.rect = self.image.get_frect(center=POS['player'])
        self.old_rect = self.rect.copy()

        self.direction = 0

    def move(self, delta_time):
        self.rect.centery += self.direction * self.speed * delta_time
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def update(self, delta_time):
        self.old_rect = self.rect.copy()
        self.get_direction()
        self.move(delta_time)


class Opponent(Paddle):
    def __init__(self, groups, ball):
        super().__init__(groups)
        self.speed = SPEED['opponent']
        self.rect = self.image.get_frect(center=POS['opponent'])
        self.ball = ball

    def get_direction(self):
        self.direction = -1 if self.rect.centery > self.ball.rect.centery else 1


class Player(Paddle):
    def __init__(self, groups):
        super().__init__(groups)
        self.speed = SPEED['player']
        self.rect = self.image.get_frect(center=POS['player'])

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
