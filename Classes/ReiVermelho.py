# 1. Módulos da biblioteca padrão
from math import cos
from random import randint

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Peca import Peca

class ReiVermelho(pygame.sprite.Sprite):
    """
    Representa a Rainha vermelha, a qual representa o chefão da fase 3.

    Attributes:
        pos_x (int): Posição horizontal do Rei Vermelho.
        pos_y (int): Posição inicial vertical do Rei Vermelho.
        t0_pecas (int): O tempo em que as peças foram lançadas.
        t0 (int): O tempo em que o Rei Vermelho foi criado.
        image (Surface): A imagem inicial do Rei Vermelho.
        mask (Mask): Mask inicial do Rei Vermelho.
        rect (Rect): Rect inicial do Rei Vermelho.
        grupo_pecas (Group): Grupo de sprites do Rei Vermelho.
        vidas (int): Vidas totais do Rei Vermelho.
    """

    def __init__(self, x : int, y : int) -> None:
        """
        Inicializa a instância da classe Rei Vermelho.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.t0_pecas = self.t0 = pygame.time.get_ticks()
        self.lancou_pecas = False
        self.image = pygame.transform.flip(LISTA_REI[0], True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_pecas = pygame.sprite.Group()
        self.vidas = 20
    
    def invocar_pecas(self) -> None:
        """
        Realiza as animações de invocar as peças, além de invocá-las.

        Returns:
            None:
        """

        # Invocando peças do céu a cada certo tempo em ms:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_pecas) % 10000 <= 6500:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[0], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)
            self.lancou_pecas = False
        elif (self.t1 - self.t0_pecas) % 10000 <= 8000:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[1], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)
            if not self.lancou_pecas:
                for _ in range(randint(5, 8)):
                    self.grupo_pecas.add(Peca())
                self.lancou_pecas = True
        elif (self.t1 - self.t0_pecas) % 10000 < 10000:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[0], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)

        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    def movimentar(self) -> None:
        """
        Realiza a movimentação da Rainha Vermelha em MHS vertical.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)
     
    def update(self) -> None:
        """
        Atualiza o Rei Vermelho.

        Returns:
            None:
        """
        
        # Invoca as peças e realiza as animações:
        self.invocar_pecas()

        # Movimenta o Rei Vermelho em MHS:
        self.movimentar()

        # Dá kill no Rei Vermelho se suas vidas forem esgotadas:
        if self.vidas <= 0:
            self.kill()

        # Atualiza a mask do Rei vermelho:
        self.mask = pygame.mask.from_surface(self.image)