# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class PlataformaRainha(pygame.sprite.Sprite):
    """
    Plataforma na qual a Rainha Vermelha se apoia:

    Attributes:
        pos_x (int): Posição horizontal da Plataforma da Rainha Vermelha.
        pos_y (int): Posição vertical inicial da Plataforma da Rainha Vermelha.
        t0 (int): O tempo em que a Plataforma foi criada.
        image (Surface): Imagem da Plataforma da Rainha Vermelha.
        mask (Mask): Mask inicial da Plataforma da Rainha Vermelha.
        rect (Rect): Rect inicial da Plataforma da Rainha vermelha.
    """

    def __init__(self) -> None:
        """
        Inicializa uma instância da classe PlataformaRainha.

        Returns:
            None:
        """
        super().__init__()
        self.pos_x = LARGURA_TELA - 256
        self.pos_y = 200
        self.t0 = pygame.time.get_ticks()
        self.image = IMAGEM_PLATAFORMA_RAINHA
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta a plataforma em MHS vertical.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)

    def update(self) -> None:
        """
        Atualiza a Plataforma da Rainha.

        Returns:
            None:
        """
        
        # Movimenta a Plataforma da Rainha Vermelha:
        self.movimentar()

        # Atualiza a mask da Plataforma da Rainha Vermelha:
        self.mask = pygame.mask.from_surface(self.image)