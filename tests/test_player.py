# tests/test_player.py

import unittest
import pygame
from player import Player

class TestPlayer(unittest.TestCase):
    """
    Classe de teste para a classe Player do jogo Space Invaders.
    """

    def setUp(self):
        """
        Configura o ambiente antes de cada teste.
        """
        pygame.init()  # Inicializa o Pygame
        self.screen = pygame.display.set_mode((800, 600))  # Configura a tela do Pygame
        self.player = Player()  # Cria uma instância do Player

    def tearDown(self):
        """
        Limpa o ambiente após cada teste.
        """
        pygame.quit()  # Encerra o Pygame

    def test_initial_position(self):
        """
        Testa se a posição inicial do Player está correta.
        """
        self.assertEqual(self.player.rect.centerx, 400)  # Verifica se o centro do Player no eixo x é 400
        self.assertEqual(self.player.rect.bottom, 580)  # Verifica se a base do Player no eixo y é 580

if __name__ == '__main__':
    unittest.main()  # Executa os testes
