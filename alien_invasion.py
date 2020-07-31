"""
Aqui será rodado o jogo
"""

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship

import game_functions as gf

ai_settings = Settings()


def run_game():
    #  Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma nave
    ship = Ship(ai_settings, screen)

    # Cria um grupo onde serão armazenados os bullets
    bullets = Group()

    #  Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

