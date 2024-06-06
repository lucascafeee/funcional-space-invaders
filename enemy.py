import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=1):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 0, 0))  # Cor vermelha para os inimigos
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(750)
        self.rect.y = random.randrange(150)
        self.speed_x = random.choice([-1, 1]) * speed
        self.speed_y = speed

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1
            self.rect.y += self.speed_y if self.rect.y < 150 else 0  # Desce apenas se estiver na parte superior

        # Desce continuamente, mas não após a fase 3
        self.rect.y += self.speed_y / 5 if self.rect.y < 150 else 0
