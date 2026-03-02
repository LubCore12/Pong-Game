from settings import *
from player import *
from ball import *

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Pong")

        self.display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()

        self.setup_sprited()

    def setup_sprited(self):
        ball = Ball(self.all_sprites, self.paddle_sprites)
        Player((self.all_sprites, self.paddle_sprites))
        Opponent((self.all_sprites, self.paddle_sprites), ball)

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(delta_time)
            self.display_screen.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_screen)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()