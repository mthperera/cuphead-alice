# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class PlataformaOvoDee(pygame.sprite.Sprite):
    """
    Representa a Plataforma do Ovo Dee.

    Attributes:
    pos_x (int): Posição horizontal em que a Plataforma é criada.
    pos_y (int): Posição vertical em que a Plataforma é criada.
    t0 (int): O tempo em que a Tela é iniciada.
    image (Surface): Imagem inicial da Plataforma.
    mask (Mask): Mask inicial da Plataforma.
    rect (Rect): Rect inicial da Plataforma.
    """

    def __init__(self, x : int, y : int) -> None:
        """ 
        Inicializa uma instância da classe PlataformaOvoDee do TweedleDee.

        Args:
        x (int): Posição x em que a plataforma é gerada.
        y (int): Posição y em que a plataforma é gerada.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = IMAGEM_CASCA_OVO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Realiza a movimentação da Plataforma em forma de MHS.
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self) -> None:
        """
        Atualiza o estado da Plataforma.
        """

        # Realiza a movimentação da plataforma:
        self.movimentar()

        # Atualiza o mask da plataforma:
        self.mask = pygame.mask.from_surface(self.image)


class PlataformaOvoDum(pygame.sprite.Sprite):
    """
    Representa a Plataforma do Ovo Dum.

    Attributes:
    pos_x (int): Posição horizontal em que a Plataforma é criada.
    pos_y (int): Posição vertical em que a Plataforma é criada.
    t0 (int): O tempo em que a Tela é iniciada.
    image (Surface): Imagem inicial da Plataforma.
    mask (Mask): Mask inicial da Plataforma.
    rect (Rect): Rect inicial da Plataforma.
    """

    def __init__(self, x : int, y : int) -> None:
        """ 
        Inicializa uma instância da classe PlataformaOvoDum do TweedleDum.

        Args:
        x (int): Posição x em que a plataforma é gerada.
        y (int): Posição y em que a plataforma é gerada.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = pygame.transform.flip(IMAGEM_CASCA_OVO, True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Realiza a movimentação da Plataforma em forma de MHS.
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self) -> None:
        """
        Atualiza o estado da Plataforma.
        """

        # Realiza a movimentação da plataforma:
        self.movimentar()

        # Atualiza o mask da plataforma:
        self.mask = pygame.mask.from_surface(self.image)
