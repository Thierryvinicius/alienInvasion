import pygame


class Ship():
    def __init__(self, screen):
        # inicializo a nave e defino sua posição inicial
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')  # armazeno a superfície que representa a nave
        self.rect = self.image.get_rect()  # obtenho o retangulo da imagem
        self.screen_rect = screen.get_rect()  # armazeno o retangulo da tela
        # inicia cada nova aeronave na parte inferior da tela
        self.rect.centerx = self.screen_rect.centerx  # coordenada x do centro da aeronave = x do retangulo da tela
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1


    def blitme(self):
        # desenha a espaçonave em sua posição atual
        self.screen.blit(self.image, self.rect)

