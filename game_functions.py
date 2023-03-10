import sys
import pygame

def check_events(ship):
    #responde a eventos da tecla e mouse
    for event in pygame.event.get(): # acessar os eventos que o PyGame detecta
        if event.type == pygame.QUIT:
            sys.exit() # fechar jogo
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(game_settings, screen, ship):
    pygame.display.flip()  # atualiza a janela
    screen.fill(game_settings.bg_color)  # cor fundo janela
    ship.blitme()