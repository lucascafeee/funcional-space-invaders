import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(750)
        self.rect.y = random.randrange(150)
        self.speed_x = random.choice([-1, 1])  
        self.speed_y = 1  
        self.max_speed = 1  

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > 800 or self.rect.left < 0:
            self.speed_x *= -1
            self.rect.y += self.speed_y

    def increase_speed(self):
        if abs(self.speed_x) < self.max_speed:
            self.speed_x *= 1.1
