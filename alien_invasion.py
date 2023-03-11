import pygame
from settings import Settings  # importo as configurações
from ship import Ship  # importo a nave
import game_functions as gf


def run_game():
    pygame.init()  # inicialização do fundamental
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # janela
    pygame.display.set_caption("Alien Invasion")  # nome da janela
    ship = Ship(screen)  # nave

    # inicialização do game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings, screen, ship)


run_game()
