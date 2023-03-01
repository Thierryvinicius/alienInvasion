import pygame


class Ship():
    def __init__(self, screen):
        # inicializo a nave e defino sua posição inicial
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp') # armazeno a superfície que representa a nave
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # inicia cada nova aeronave na parte inferior da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # desenha a espaçonave em sua posição atual
        self.screen.blit(self.image, self.rect)
