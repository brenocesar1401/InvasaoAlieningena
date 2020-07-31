import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Uma classe que administra projéteis disparadaos pela espaçonave"""

    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto para o projetil na posição atual da nave"""
        super(Bullet, self).__init__()
        self.screen = screen

        """Cria um reganulo para o projetil em (0, 0) e em seguida define a posicao correta"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        """Armazena a posição do projétil como um valor decima"""
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projetil para cima na tela"""
        # Atualiza a posição decimal do projetil
        self.y -= self.speed_factor
        # Atualiza a posicacao de rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
