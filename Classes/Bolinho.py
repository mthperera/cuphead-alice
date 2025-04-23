# 1. Módulos da biblioteca padrão
from math import cos, sin, radians

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *


class Bolinho(pygame.sprite.Sprite):
    """
    Representa a Classe Bolinho da Alice.

    Attributes:
        image (Surface): Imagem Inicial do Bolinho.
        mask (Mask): Mask Inicial do Bolinho.
        rect (Rect): Rect Inicial do Bolinho.
        velocidade (int): Módulo da velocidade do Bolinho.
        velocidade_x (float): Velocidade horizontal do Bolinho.
        velocidade_y (float): Velocidade vertical do Bolinho.
        t0 (int): O tempo em que a Tela é iniciada.
    """

    def __init__(self, x : int, y : int, angulo : float) -> None:
        """
        Inicializa uma instância da classe Bolinho.

        Args:
            x (int): Posição horizontal inicial do Bolinho.
            y (int): Posição verticial inicial do Bolinho.
            angulo (float): Ângulo em graus realizado pelo analógico esquerdo.
        
        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = BOLINHO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.velocidade = 500
        self.velocidade_x = self.velocidade * cos(radians(angulo))
        self.velocidade_y = - self.velocidade * sin(radians(angulo))
        self.t0 = pygame.time.get_ticks()

    def movimentar(self) -> None:
        """
        Realiza a movimentação do Bolinho.

        Returns:
            None
        """
        
        # Movimento retilíneo do Bolinho:
        now = pygame.time.get_ticks()
        self.dt = (now - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = now

    def update(self) -> None:
        """
        Atualiza o estado do bolinho:

        Returns:
            None
        """
        
        # Realiza a movimentação do Bolinho:
        self.movimentar()
        
        # Dando kill no Bolinho quando ele excede os limites do mapa:
        if self.rect.x > LARGURA_TELA or self.rect.x < 0:
            self.kill()
        elif self.rect.y > ALTURA_TELA or self.rect.y < 0:
            self.kill()

        # Atualizando a mask do Bolinho:
        self.mask = pygame.mask.from_surface(self.image)