# 1. Módulos da biblioteca padrão
from math import cos, pi

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class IoioDee(pygame.sprite.Sprite):
    """
    Representa o Ioiô Dee.

    Attributes:
        pos_x (int): Posição horizontal em que o Ioiô é gerado.
        pos_y (int): Posição vertical em que o Ioiô é gerado.
        t0 (int): O tempo em que a Tela é iniciada.
        image (Surface): Imagem inicial do Ioiô.
        mask (Mask): Mask inicial do Ioiô.
        rect (Rect): Rect inicial do Ioiô.
    """

    def __init__(self, x : int, y : int) -> None:
        """ 
        Inicializa uma instância da classe Ioiô. 

        Args:
        x (int): Posição x em que o ioiô é gerado.
        y (int): Posição y em que o ioiô é gerado.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = LISTA_IOIO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta o Ioiô numa figura diferente matematicamente: Figura de Lissajous errante.

        Returns:
            None:
        """

        # Ioio fazendo uma Figura de Lissajous de curva errante por meio de dois MHS ortogonais.
        # Isso foi feito para dar uma sensação de movimento mais aleatório.
        self.rect.y = self.pos_y + 200*cos(pi/2*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 150*cos(2.5*(pygame.time.get_ticks()-self.t0)/1000)
    
    def piscar(self) -> None:
        """
        Realiza o movimento do piscar do olho do Ioiô.

        Returns:
            None
        """

        # Animação do Ioiô piscando:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = LISTA_IOIO[0]
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = LISTA_IOIO[1]

    def update(self) -> None:
        """
        Atualiza o estado do Ioiô:
        """

        # Movimenta o Ioiô:
        self.movimentar()

        # Anima o piscar do olho:
        self.piscar()

        # Atualiza a mask do Ioiô:
        self.mask = pygame.mask.from_surface(self.image)


class IoioDum(pygame.sprite.Sprite):
    """
    Representa o Ioiô Dee.

    Attributes:
        pos_x (int): Posição horizontal em que o Ioiô é gerado.
        pos_y (int): Posição vertical em que o Ioiô é gerado.
        t0 (int): O tempo em que a Tela é iniciada.
        image (Surface): Imagem inicial do Ioiô.
        mask (Mask): Mask inicial do Ioiô.
        rect (Rect): Rect inicial do Ioiô.
    """

    def __init__(self, x : int, y : int) -> None:
        """ 
        Inicializa uma instância da classe Ioiô. 

        Args:
        x (int): Posição x em que o ioiô é gerado.
        y (int): Posição y em que o ioiô é gerado.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = LISTA_IOIO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta o Ioiô numa figura diferente matematicamente: Figura de Lissajous errante.

        Returns:
            None:
        """

        # Ioio fazendo uma Figura de Lissajous de curva errante por meio de dois MHS ortogonais.
        # Isso foi feito para dar uma sensação de movimento mais aleatório.
        self.rect.y = self.pos_y + 200*cos(pi/2*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 150*cos(2.5*(pygame.time.get_ticks()-self.t0)/1000)

    def piscar(self) -> None:
        """
        Realiza o movimento do piscar do olho do Ioiô.

        Returns:
            None
        """

        # Animação do Ioiô piscando:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = pygame.transform.flip(LISTA_IOIO[0], True, False)
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = pygame.transform.flip(LISTA_IOIO[1], True, False)

    def update(self) -> None:
        """
        Atualiza o estado do Ioiô:
        """

        # Movimenta o Ioiô:
        self.movimentar()

        # Anima o piscar do olho:
        self.piscar()

        # Atualiza a mask do Ioiô:
        self.mask = pygame.mask.from_surface(self.image)