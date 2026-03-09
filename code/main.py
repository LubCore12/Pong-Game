import json

from settings import *
from player import *
from ball import *
from groups import *
import json

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Pong")

        self.display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()

        try:
            with open(join('data', 'score.json'), 'r', encoding="utf-8") as score_file:
                self.score = json.load(score_file)
        except FileNotFoundError:
            self.score = {
                'player': 0,
                'opponent': 0
            }

        self.font = pygame.font.Font(None, 160)

        self.setup_sprited()

    def display_score(self):
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_screen.blit(player_surf, player_rect)

        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center=(WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_screen.blit(opponent_surf, opponent_rect)

        pygame.draw.line(self.display_screen, COLORS['bg detail'], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 7)

    def update_score(self, side):
        self.score[side] += 1

    def setup_sprited(self):
        ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        Player((self.all_sprites, self.paddle_sprites))
        Opponent((self.all_sprites, self.paddle_sprites), ball)

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                    with open(join('data', 'score.json'), 'w', encoding="utf-8") as score_file:
                        json.dump(self.score, score_file )

            self.all_sprites.update(delta_time)
            self.display_screen.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()