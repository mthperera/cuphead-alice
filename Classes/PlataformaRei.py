# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class PlataformaRei(pygame.sprite.Sprite):
    """
    Plataforma na qual o Rei Vermelho se apoia:

    Attributes:
        pos_x (int): Posição horizontal da Plataforma do Rei Vermelho.
        pos_y (int): Posição vertical inicial da Plataforma do Rei Vermelho.
        t0 (int): O tempo em que a Plataforma foi criada.
        image (Surface): Imagem da Plataforma do Rei Vermelho.
        mask (Mask): Mask inicial da Plataforma do Rei Vermelho.
        rect (Rect): Rect inicial da Plataforma do Rei Vermelho.
    """
    
    def __init__(self) -> None:
        """
        Inicializa uma instância da classe PlataformaRei.

        Returns:
            None:
        """
        super().__init__()
        self.pos_x = 0
        self.pos_y = 200
        self.t0 = pygame.time.get_ticks()
        self.image = IMAGEM_PLATAFORMA_REI
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
        Atualiza a Plataforma do Rei.

        Returns:
            None:
        """
        
        # Movimenta a Plataforma do Rei Vermelho:
        self.movimentar()

        # Atualiza a mask da Plataforma do Rei Vermelho:
        self.mask = pygame.mask.from_surface(self.image)