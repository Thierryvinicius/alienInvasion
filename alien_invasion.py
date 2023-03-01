import pygame
import sys
from settings import Settings # importo as configurações
from ship import Ship # importo a nave

def run_game():
    pygame.init()  # inicializo o jogo e crio obj na tela
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # inicialização do game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        screen.fill(game_settings.bg_color)
        ship.blitme()



run_game()