import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from functools import reduce

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0

def shoot():
    bullet = Bullet(player.rect.centerx, player.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

apply_to_enemies = lambda func, enemies: [func(enemy) for enemy in enemies]

def increase_speed(enemy):
    enemy.increase_speed()
    return enemy

fatorial = (lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))(lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))

add_to_score = lambda x: (lambda y: x + y)
increment_score = add_to_score(score)
score = increment_score(1)

filter_enemies = lambda enemies: [enemy for enemy in enemies if enemy.rect.y < 600]

key_map = lambda: {
    pygame.K_LEFT: -5,
    pygame.K_RIGHT: 5
}

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))

even = list(filter(lambda x: x % 2 == 0, numbers))


summation = reduce(lambda x, y: x + y, numbers)

class Monad:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return Monad(func(self.value))

    def __str__(self):
        return f'Monad({self.value})'

score_monad = Monad(score).bind(lambda x: x + 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    apply_to_enemies(increase_speed, enemies)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, f'Score: {score}', 18, 400, 10)
    pygame.display.flip()

pygame.quit()
