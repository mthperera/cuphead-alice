# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceTweedle import AliceTweedle
from Classes.Ovo import Ovo

class TweedleDee(pygame.sprite.Sprite):
    """
    Representa o personagem TweedleDee, o qual é um dos chefões da fase 2.

    Attributes:
        x (int): Posição x do topleft do TweedleDee.
        y (int): Posição y do topleft do TweedleDee.
        alice (AliceTweedle): Personagem AliceTweedle.
        t0_ovo (int): Tempo em que o ovo é lançado.
        t0 (int): O tempo em que a Tela é iniciada.
        image (Surface): Imagem inicial do TweedleDee.
        mask (Mask): Mask inicial do TweedleDee.
        grupo_ovos (Group): Grupo dos ovos do TweedleDee.
        vidas (int): Vidas do TweedleDee.
    """

    def __init__(self, x : int, y : int, alice : AliceTweedle) -> None:
        """ 
        Inicializa uma instância da classe TweedleDee.

        Args:
            x (int): Posição x do topleft do TweedleDee.
            y (int): Posição y do topleft do TweedleDee.
            alice (AliceTweedle): Personagem AliceTweedle.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.alice = alice
        self.t0_ovo = self.t0 = pygame.time.get_ticks()
        self.lancou_ovo = False
        self.image = LISTA_TEEDLE_OVO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_ovos = pygame.sprite.Group()
        self.vidas = 15

    def jogar_ovo(self) -> None:
        """ 
        Joga ovos direcionados à AliceTweedle a cada período de tempo.

        Returns:
            None:
        """

        # Lançando ovo a cada certo período em ms:
        self.t1 = pygame.time.get_ticks()

        dt = (self.t1 - self.t0_ovo) % 3000
        indice = dt // 600
        indice = 5 - indice if indice > 3 else indice
        self.image = LISTA_TEEDLE_OVO[indice]

        if indice == 0:
            self.lancou_ovo = 0
        if indice == 3:
            if not self.lancou_ovo:
                self.grupo_ovos.add(Ovo(155, 65, self.alice.rect.centerx - 120, self.alice.rect.centery - 120))
                self.grupo_ovos.add(Ovo(155, 65, self.alice.rect.centerx, self.alice.rect.centery))
                self.grupo_ovos.add(Ovo(155, 65, self.alice.rect.centerx + 120, self.alice.rect.centery + 120))
                self.lancou_ovo = True

        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    def movimentar(self) -> None:
        """ 
        Movimenta o Tweedle em MHS vertical.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self) -> None:
        """
        Atualiza o estado do Tweedle e invocar os ovos

        Returns:
            None:
        """
        
        # Jogando os ovos:
        self.jogar_ovo()

        # Movimentando o Tweedle:
        self.movimentar()

        # Eliminando o Tweedle do grupo caso ela tenha vida menor do que 0:
        if self.vidas <= 0:
            self.kill()

        # Refazendo a mask:
        self.mask = pygame.mask.from_surface(self.image)


class TweedleDum(pygame.sprite.Sprite):
    """
    Representa o personagem TweedleDee, o qual é um dos chefões da fase 2.

    Attributes:
        x (int): Posição x do topleft do TweedleDum.
        y (int): Posição y do topleft do TweedleDum.
        alice (AliceTweedle): Personagem AliceTweedle.
        t0_ovo (int): Tempo em que o ovo é lançado.
        t0 (int): O tempo em que a Tela é iniciada.
        image (Surface): Imagem inicial do TweedleDum.
        mask (Mask): Mask inicial do TweedleDum.
        grupo_ovos (Group): Grupo dos ovos do TweedleDum.
        vidas (int): Vidas totais do TweedleDum.
    """

    def __init__(self, x : int, y : int, alice : AliceTweedle) -> None:
        """ 
        Inicializa uma instância da classe TweedleDum. 

        Args:
            x (int): Posição x do topleft do TweedleDum.
            y (int): Posição y do topleft do TweedleDum.
            alice (AliceTweedle): Personagem AliceTweedle.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.alice = alice
        self.t0_ovo = self.t0 = pygame.time.get_ticks()
        self.lancou_ovo = False
        self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[0], True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_ovos = pygame.sprite.Group()
        self.vidas = 15
    
    def jogar_ovo(self) -> None:
        """ 
        Joga ovos direcionados à AliceTweedle a cada período de tempo.

        Returns:
            None:
        """

        # Lançando ovo a cada certo período em ms:
        self.t1 = pygame.time.get_ticks()

        dt = (self.t1 - self.t0_ovo) % 3000
        indice = dt // 600
        indice = 5 - indice if indice > 3 else indice
        self.image = LISTA_TEEDLE_OVO[indice]

        if indice == 0:
            self.lancou_ovo = 0
        if indice == 3:
            if not self.lancou_ovo:
                self.grupo_ovos.add(Ovo(LARGURA_TELA - 155, 65, self.alice.rect.centerx - 120, self.alice.rect.centery - 120))
                self.grupo_ovos.add(Ovo(LARGURA_TELA - 155, 65, self.alice.rect.centerx, self.alice.rect.centery))
                self.grupo_ovos.add(Ovo(LARGURA_TELA - 155, 65, self.alice.rect.centerx + 120, self.alice.rect.centery + 120))
                self.lancou_ovo = True

        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    def movimentar(self) -> None:
        """ 
        Movimenta o Tweedle em MHS vertical.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self) -> None:
        """
        Atualiza o estado do Tweedle e invocar os ovos

        Returns:
            None:
        """
        
        # Jogando os ovos:
        self.jogar_ovo()

        # Movimentando o Tweedle:
        self.movimentar()

        # Eliminando o Tweedle do grupo caso ela tenha vida menor do que 0:
        if self.vidas <= 0:
            self.kill()

        # Refazendo a mask:
        self.mask = pygame.mask.from_surface(self.image)