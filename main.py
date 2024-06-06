import pygame
import random
import time
from player import Player
from enemy import Enemy
from bullet import Bullet
from functools import reduce
import os

# Suprime avisos de log irrelevantes
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Inicializa o Pygame
pygame.init()

# Configura a tela do jogo
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Função para desenhar texto na tela
def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Cria grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Cria a instância do Player
player = Player()
all_sprites.add(player)

# Função para criar inimigos
def create_enemies(num_enemies, enemy_speed):
    for _ in range(num_enemies):
        enemy = Enemy(speed=enemy_speed)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Inicializa a primeira fase
current_phase = 1
num_enemies = 8
enemy_speed = 1
create_enemies(num_enemies, enemy_speed)
start_time = time.time()

score = 0

# Função para atirar
def shoot():
    bullet = Bullet(player.rect.centerx, player.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

# Função lambda de alta ordem
apply_to_enemies = lambda func, enemies: [func(enemy) for enemy in enemies]

# Função lambda recursiva
fatorial = (lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))(lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))

# Função lambda com currying
add_to_score = lambda x: (lambda y: x + y)
increment_score = add_to_score(score)
score = increment_score(1)

# List Comprehension dentro de uma Lambda
filter_enemies = lambda enemies: [enemy for enemy in enemies if enemy.rect.y < 600]

# Dicionário dentro de uma Lambda
key_map = lambda: {
    pygame.K_LEFT: -5,
    pygame.K_RIGHT: 5
}

# Functor map para elevar ao quadrado
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# Functor filter para selecionar pares
even = list(filter(lambda x: x % 2 == 0, numbers))

# Functor reduce para somar
summation = reduce(lambda x, y: x + y, numbers)

# Monad
class Monad:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return Monad(func(self.value))

    def __str__(self):
        return f'Monad({self.value})'

score_monad = Monad(score).bind(lambda x: x + 1)

running = True
game_over = False
time_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()

    if not game_over:
        # Atualiza os sprites
        all_sprites.update()

        # Verifica colisão entre balas e inimigos
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for hit in hits:
            score += 1

        # Verifica colisão entre inimigos e player
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            draw_text(screen, 'Você perdeu!', 64, 400, 300, RED)
            pygame.display.flip()
            pygame.time.wait(2000)
            game_over = True

        # Verifica se todos os inimigos foram destruídos
        if len(enemies) == 0:
            current_phase += 1
            num_enemies += 4  # Aumenta o número de inimigos a cada fase
            enemy_speed += 1  # Aumenta a velocidade dos inimigos a cada fase
            create_enemies(num_enemies, enemy_speed)
            start_time = time.time()  # Reinicia o temporizador para a nova fase

        # Verifica se o tempo limite foi atingido
        elapsed_time = time.time() - start_time
        if elapsed_time > 30:
            draw_text(screen, 'O tempo acabou, você perdeu!!', 64, 400, 300, RED)
            pygame.display.flip()
            pygame.time.wait(2000)
            game_over = True
            time_over = True

    # Desenha e atualiza a tela
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, f'Pontuação: {score}', 18, 400, 10)
    draw_text(screen, f'Fase: {current_phase}', 18, 400, 30)
    draw_text(screen, f'Tempo atual (max 30seg): {int(elapsed_time)}', 18, 400, 50)
    pygame.display.flip()

    if game_over and time_over:
        running = False

pygame.quit()
