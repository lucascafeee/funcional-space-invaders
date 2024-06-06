# tests/test_main.py

import unittest
import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

class TestMain(unittest.TestCase):
    """
    Classe de teste para a configuração inicial do jogo Space Invaders.
    """

    def setUp(self):
        """
        Configura o ambiente antes de cada teste.
        """
        pygame.init()  # Inicializa o Pygame
        self.screen = pygame.display.set_mode((800, 600))  # Configura a tela do Pygame
        self.all_sprites = pygame.sprite.Group()  # Cria um grupo para todos os sprites
        self.enemies = pygame.sprite.Group()  # Cria um grupo para os inimigos
        self.player = Player()  # Cria uma instância do Player
        self.all_sprites.add(self.player)  # Adiciona o Player ao grupo de todos os sprites
        for _ in range(8):
            enemy = Enemy()  # Cria instâncias dos Enemies
            self.all_sprites.add(enemy)  # Adiciona cada Enemy ao grupo de todos os sprites
            self.enemies.add(enemy)  # Adiciona cada Enemy ao grupo de inimigos
        self.score = 0  # Inicializa o placar

    def tearDown(self):
        """
        Limpa o ambiente após cada teste.
        """
        pygame.quit()  # Encerra o Pygame

    def test_initial_setup(self):
        """
        Testa se a configuração inicial do jogo está correta.
        """
        self.assertEqual(len(self.all_sprites), 9)  # Verifica se o número total de sprites é 9 (1 player + 8 enemies)
        self.assertEqual(len(self.enemies), 8)  # Verifica se o número de inimigos é 8

if __name__ == '__main__':
    unittest.main()  # Executa os testes
