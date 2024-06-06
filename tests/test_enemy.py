# tests/test_enemy.py

import unittest
import pygame
from enemy import Enemy

class TestEnemy(unittest.TestCase):
    """
    Classe de teste para a classe Enemy do jogo Space Invaders.
    """

    def setUp(self):
        """
        Configura o ambiente antes de cada teste.
        """
        pygame.init()  # Inicializa o Pygame
        self.screen = pygame.display.set_mode((800, 600))  # Configura a tela do Pygame
        self.enemy = Enemy()  # Cria uma instância do Enemy

    def tearDown(self):
        """
        Limpa o ambiente após cada teste.
        """
        pygame.quit()  # Encerra o Pygame

    def test_initial_position(self):
        """
        Testa se a posição inicial do Enemy está correta.
        """
        self.assertTrue(0 <= self.enemy.rect.x < 750)  # Verifica se a posição x do Enemy está no intervalo correto
        self.assertTrue(0 <= self.enemy.rect.y < 150)  # Verifica se a posição y do Enemy está no intervalo correto

    def test_initial_speed(self):
        """
        Testa se a velocidade inicial do Enemy está correta.
        """
        self.assertIn(self.enemy.speed_x, [-1, 1])  # Verifica se a velocidade x é -1 ou 1
        self.assertEqual(self.enemy.speed_y, 1)  # Verifica se a velocidade y é 1

if __name__ == '__main__':
    unittest.main()  # Executa os testes
