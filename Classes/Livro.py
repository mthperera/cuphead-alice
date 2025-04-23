# 1. Módulos da biblioteca padrão
from math import sqrt
from random import choice

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaVermelha import AliceRainhaVermelha

class Livro(pygame.sprite.Sprite):
    """
    Representa o livro que é jogado pela Rainha vermelha em direção à Alice.

    Attributes:
        pos_x (int): Posição inicial horizontal do livro.
        pos_y (int): Posição inicial vertical do livro.
        dx (int): Distância horizontal entre a Alice e o livro.
        dy (int): Distância vertical entre a Alice e o livro.
        velocidade_x (float): Velocidade horizontal do livro (em direção à Alice).
        velocidade_y (float): Velocidade vertical do livro (em direção à Alice).
        t0 (int): O tempo em que o livro é criado.
        image (Surface): A imagem do livro randomizada (a qual pode variar diante de cores disponíveis).
        mask (Mask): Mask inicial do livro.
        rect (Rect): Rect inicial do livro.
    """

    def __init__(self, x : int, y : int, alice : AliceRainhaVermelha) -> None:
        """
        Inicializa uma instância do livro.

        Args:
            x (int): Posição inicial horizontal do livro.
            y (int): Posição inicial vertical do livro.
            alice (AlicerainhaVermelha): Personagem Alice que enfrenta a Rainha Vermelha.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.dx = alice.rect.centerx - self.pos_x
        self.dy = alice.rect.centery - self.pos_y
        self.velocidade_x = self.dx/sqrt(self.dx**2 + self.dy**2) * 450
        self.velocidade_y = self.dy/sqrt(self.dx**2 + self.dy**2) * 450
        self.t0 = pygame.time.get_ticks()
        self.image = choice(LISTA_LIVROS)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta o livro em direção à Alice em movimento retilíneo uniforme.

        Returns:
            None:
        """

        # Esse movimento inicia em direção ao personagem, já que forçamos o vetor velocidade ser radial em coordenadas polares.
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1

    def update(self) -> None:
        """
        Atualiza estado dos livros.

        Returns:
            None:
        """
        
        # Movimenta os livros:
        self.movimentar()
        
        # Dando kill nos livros que ficam fora do limite do mapa:
        if self.rect.top > ALTURA_TELA or self.rect.bottom < 0:
            self.kill()
        elif self.rect.right < 0 or self.rect.left > LARGURA_TELA:
            self.kill()
        
        # Atualizando mask dos livros:
        self.mask = pygame.mask.from_surface(self.image)