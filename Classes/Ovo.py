# 1. Módulos da biblioteca padrão
from math import sqrt
from random import choice

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *


class Ovo(pygame.sprite.Sprite):
    """
    Representa o ovo que é a arma dos irmãos Tweedle.

    Attributes:
        pos_x (int): Posição x em que o ovo é gerado.
        pos_y (int): Posição y em que o ovo é gerado.
        dx (int): Distância horizontal inicial entre o ovo e o alvo.
        dy (int): Distância verticial inicial entre o ovo e o alvo.
        velocidade_x (float): Velocidade horizontal inicial do ovo.
        velocidade_y (float): Velocidade verticial inicial do ovo.
        t0 (int): O tempo em que a Tela é iniciada.
        image (Surface): Imagem do ovo randomizada (cor aleatórias dento das possíveis).
        mask (Mask): Mask inicial do ovo.
        rect (Rect): Rect inicial do ovo.
    """

    def __init__(self, x : int, y : int, x_alvo : int, y_alvo : int) -> None:
        """ 
        Inicializa uma instância da classe Ovo. 

        Args:
        x (int): Posição x em que o ovo é gerado.
        y (int): Posição y em que o ovo é gerado.
        x_alvo (int): Posição x do alvo.
        y_alvo (int): posição y do alvo.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.dx = x_alvo - self.pos_x
        self.dy = y_alvo - self.pos_y
        self.velocidade_x = self.dx/sqrt(self.dx**2 + self.dy**2) * 450
        self.velocidade_y = self.dy/sqrt(self.dx**2 + self.dy**2) * 450
        self.t0 = pygame.time.get_ticks()
        self.image = choice(LISTA_OVOS)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta o personagem com velocidade inicial sendo um vetor radial em direção ao alvo.

        Returns:
            None:
        """

        # Esse movimento retilíneo inicia em direção ao personagem, já que forçamos o vetor velocidade ser radial em coordenadas polares.
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1

    def update(self) -> None:
        """
        Atualiza o estado do ovo.
        """
        
        # Movimenta o ovo:
        self.movimentar()
        
        # Dando kill no ovo quando ele excede os limites do mapa:
        if self.rect.y > ALTURA_TELA or self.rect.y < 0:
            self.kill()
        elif self.rect.x < 0 or self.rect.x > LARGURA_TELA:
            self.kill()
        
        # Atualiza o mask do ovo:
        self.mask = pygame.mask.from_surface(self.image)