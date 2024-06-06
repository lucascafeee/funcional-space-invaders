# tests/test_bullet.py

import unittest
import pygame
from bullet import Bullet

class TestBullet(unittest.TestCase):
    """
    Classe de teste para a classe Bullet do jogo Space Invaders.
    """

    def setUp(self):
        """
        Configura o ambiente antes de cada teste.
        """
        pygame.init()  # Inicializa o Pygame
        self.screen = pygame.display.set_mode((800, 600))  # Configura a tela do Pygame
        self.bullet = Bullet(400, 580)  # Cria uma instância da Bullet com posição inicial

    def tearDown(self):
        """
        Limpa o ambiente após cada teste.
        """
        pygame.quit()  # Encerra o Pygame

    def test_initial_position(self):
        """
        Testa se a posição inicial da Bullet está correta.
        """
        self.assertEqual(self.bullet.rect.centerx, 400)  # Verifica se o centro da Bullet no eixo x é 400
        self.assertEqual(self.bullet.rect.bottom, 580)  # Verifica se a base da Bullet no eixo y é 580

    def test_initial_speed(self):
        """
        Testa se a velocidade inicial da Bullet está correta.
        """
        self.assertEqual(self.bullet.speed_y, -10)  # Verifica se a velocidade y é -10

if __name__ == '__main__':
    unittest.main()  # Executa os testes
