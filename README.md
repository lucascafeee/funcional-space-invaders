# Space Invaders em Pygame

Este é um projeto de um jogo de Space Invaders desenvolvido com a biblioteca Pygame. O objetivo do jogo é destruir os inimigos antes que eles alcancem a parte inferior da tela. O jogo tem múltiplas fases com dificuldade crescente, e o jogador perde se não eliminar todos os inimigos em 30 segundos ou se for atingido por um inimigo.

## Requisitos Funcionais e Não-Funcionais

### Requisitos Funcionais

1. O jogador deve ser capaz de mover-se para a esquerda e para a direita.
2. O jogador deve ser capaz de disparar projéteis.
3. Inimigos devem aumentar a velocidade gradualmente.
4. A pontuação deve ser atualizada conforme os inimigos são destruídos.
5. O jogador avança para a próxima fase após destruir todos os inimigos.
6. O jogo deve exibir uma mensagem de derrota se o jogador não eliminar todos os inimigos em 30 segundos.

### Requisitos Não-Funcionais

1. O jogo deve ser executado sem travamentos ou bugs.
2. O código deve ser bem documentado e seguir boas práticas de programação.
3. O jogo deve ser disponibilizado em um repositório GitHub.
4. O código deve ser feito em programação funcional

## Instalação

Para rodar o jogo, você precisará ter o Python e a biblioteca Pygame instalados. Siga os passos abaixo para instalar as dependências e executar o jogo.

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/space-invaders.git
    cd space-invaders
    ```

2. Instale a biblioteca Pygame:

    ```sh
    pip install pygame
    ```

3. Execute o jogo:

    ```sh
    python main.py
    ```

## Uso

- Utilize as teclas de seta esquerda e direita para mover o jogador.
- Pressione a barra de espaço para disparar projéteis.
- Elimine todos os inimigos antes que eles alcancem a parte inferior da tela ou o tempo limite de 30 segundos.

## Estrutura do Código

- `main.py`: Arquivo principal que inicializa o jogo e contém o loop principal.
- `player.py`: Define a classe Player.
- `enemy.py`: Define a classe Enemy.
- `bullet.py`: Define a classe Bullet.
- `images/`: Diretório contendo as imagens para o jogador e os inimigos (`player.png` e `enemy.png`).

## Conceitos Funcionais Utilizados

O jogo utiliza vários conceitos de programação funcional, incluindo:

1. **Função lambda de alta ordem**:
   - `apply_to_enemies`: Aplica uma função a todos os inimigos.
     ```python
     apply_to_enemies = lambda func, enemies: [func(enemy) for enemy in enemies]
     ```

2. **Função lambda recursiva**:
   - `fatorial`: Calcula o fatorial de um número usando recursão.
     ```python
     fatorial = (lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))(lambda f: (lambda x: 1 if x == 0 else x * f(f)(x - 1)))
     ```

3. **Função lambda com currying**:
   - `add_to_score`: Função curried que adiciona pontos ao score.
     ```python
     add_to_score = lambda x: (lambda y: x + y)
     increment_score = add_to_score(score)
     score = increment_score(1)
     ```

4. **List Comprehension dentro de uma Lambda**:
   - `filter_enemies`: Filtra inimigos cuja posição `y` é menor que 600.
     ```python
     filter_enemies = lambda enemies: [enemy for enemy in enemies if enemy.rect.y < 600]
     ```

5. **Dicionário dentro de uma Lambda**:
   - `key_map`: Retorna um dicionário que mapeia teclas a valores.
     ```python
     key_map = lambda: {
         pygame.K_LEFT: -5,
         pygame.K_RIGHT: 5
     }
     ```

6. **Functores**:
   - `map`: Para elevar números ao quadrado.
     ```python
     numbers = [1, 2, 3, 4, 5]
     squared = list(map(lambda x: x ** 2, numbers))
     ```
   - `filter`: Para selecionar números pares.
     ```python
     even = list(filter(lambda x: x % 2 == 0, numbers))
     ```
   - `reduce`: Para somar números.
     ```python
     summation = reduce(lambda x, y: x + y, numbers)
     ```

7. **Monad**:
   - `Monad`: Classe que encapsula um valor e permite encadear operações.
     ```python
     class Monad:
         def __init__(self, value):
             self.value = value

         def bind(self, func):
             return Monad(func(self.value))

         def __str__(self):
             return f'Monad({self.value})'

     score_monad = Monad(score).bind(lambda x: x + 1)
     ```