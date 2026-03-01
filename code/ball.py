from settings import *
from random import choice, uniform


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)

        self.image = pygame.Surface(SIZE['ball'], flags=pygame.SRCALPHA)
        pygame.draw.circle(self.image, COLORS['ball'], (SIZE['ball'][0] / 2, SIZE['ball'][1] / 2), SIZE['ball'][0] / 2)
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.direction = pygame.Vector2(choice((-1, 1)), uniform(0.7, 0.8) * choice((-1, 1)))

        self.paddle_sprites = paddle_sprites

    def move(self, delta_time):
        self.wall_collision()
        self.rect.center += self.direction * SPEED['ball'] * delta_time

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y = 1
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y = -1

    def update(self, delta_time):
        self.move(delta_time)
