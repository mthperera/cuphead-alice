# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Tweedle import *

class PlataformaOvoDee(pygame.sprite.Sprite):
    """
    Representa a Plataforma do Ovo Dee.

    Attributes:
    pos_x (int): Posição horizontal em que a Plataforma é criada.
    pos_y (int): Posição vertical em que a Plataforma é criada.
    tweedledee (TweedleDee): Instância de TweedleDee.
    t0 (int): O tempo em que a Tela é iniciada.
    t0_morte (int): O tempo em que o Tweedle morre.
    t0_morte_movimentacao (int): O tempo que é usado para a movimentação de morte.
    velocidade_angular (int): A velocidade omega de rotação angular da Plataforma ao cair.
    velocidade_y (int): A velocidade de queda da Plataforma.
    self.angulo (float): O ângulo de rotação da plataforma caindo.
    image (Surface): Imagem inicial da Plataforma.
    mask (Mask): Mask inicial da Plataforma.
    rect (Rect): Rect inicial da Plataforma.
    """

    def __init__(self, x : int, y : int, tweedledee : TweedleDee) -> None:
        """ 
        Inicializa uma instância da classe PlataformaOvoDee do TweedleDee.

        Args:
        x (int): Posição x em que a plataforma é gerada.
        y (int): Posição y em que a plataforma é gerada.
        tweedledee (TweedleDee): Instância de TweedleDee.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.tweedle_dee = tweedledee
        self.t0 = pygame.time.get_ticks()
        self.t0_morte = self.t0_morte_movimentacao = pygame.time.get_ticks()
        self.velocidade_angular = 15
        self.velocidade_y = 100
        self.angulo = 0
        self.vivo = True
        self.image = IMAGEM_CASCA_OVO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Realiza a movimentação da Plataforma em forma de MHS.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def movimentar_morte(self) -> None:
        """
        Realiza a movimentação e a animação da plataforma quando o Tweedle morre.

        Returns:
            None:
        """

        # Realizando a movimentação angular:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_morte) / 1000
        self.angulo += self.velocidade_angular * dt
        self.t0_morte = now

        # Realizando a movimentação vertical:
        dt_mov = (now - self.t0_morte_movimentacao) / 1000
        self.rect.y += self.velocidade_y * dt_mov
        self.t0_morte_movimentacao = now

        # Realizando a inversão do movimento angular:
        if self.angulo > 45:
            self.velocidade_angular = -abs(self.velocidade_angular)
        elif self.angulo < -45:
            self.velocidade_angular = abs(self.velocidade_angular)
        
        # Realizando a animação:
        centro = self.rect.center
        self.image = pygame.transform.rotate(IMAGEM_CASCA_OVO, self.angulo)
        self.rect = self.image.get_rect(center=centro)
    
    def update(self) -> None:
        """
        Atualiza o estado da Plataforma.

        Returns:
            None:
        """

        # Realiza a movimentação da plataforma:
        if self.vivo:
            self.movimentar()
        else:
            self.movimentar_morte()

        # Mudando o estado de vivo quando morrer:
        if self.tweedle_dee.vidas <= 0 and self.vivo:
            self.t0_morte = self.t0_morte_movimentacao = pygame.time.get_ticks()
            self.vivo = False
        
        # Dando kill quando excede os limites:
        if self.rect.top > ALTURA_TELA:
            self.kill()

        # Atualiza o mask da plataforma:
        self.mask = pygame.mask.from_surface(self.image)


class PlataformaOvoDum(pygame.sprite.Sprite):
    """
    Representa a Plataforma do Ovo Dum.

    Attributes:
    pos_x (int): Posição horizontal em que a Plataforma é criada.
    pos_y (int): Posição vertical em que a Plataforma é criada.
    tweedledum (TweedleDum): Instância de TweedleDum.
    t0 (int): O tempo em que a Tela é iniciada.
    t0_morte (int): O tempo em que o Tweedle morre.
    t0_morte_movimentacao (int): O tempo que é usado para a movimentação de morte.
    velocidade_angular (int): A velocidade omega de rotação angular da Plataforma ao cair.
    velocidade_y (int): A velocidade de queda da Plataforma.
    self.angulo (float): O ângulo de rotação da plataforma caindo.
    image (Surface): Imagem inicial da Plataforma.
    mask (Mask): Mask inicial da Plataforma.
    rect (Rect): Rect inicial da Plataforma.
    """

    def __init__(self, x : int, y : int, tweedledum : TweedleDum) -> None:
        """ 
        Inicializa uma instância da classe PlataformaOvoDum do TweedleDum.

        Args:
        x (int): Posição x em que a plataforma é gerada.
        y (int): Posição y em que a plataforma é gerada.
        tweedledum (TweedleDum): Instância de TweedleDum.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.tweedle_dum = tweedledum
        self.t0 = pygame.time.get_ticks()
        self.t0_morte = self.t0_morte_movimentacao = pygame.time.get_ticks()
        self.velocidade_angular = 25
        self.velocidade_y = 100
        self.angulo = 0
        self.vivo = True
        self.image = pygame.transform.flip(IMAGEM_CASCA_OVO, True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Realiza a movimentação da Plataforma em forma de MHS.
        
        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)

    def movimentar_morte(self) -> None:
        """
        Realiza a movimentação e a animação da plataforma quando o Tweedle morre.

        Returns:
            None:
        """

        # Realizando a movimentação angular:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_morte) / 1000
        self.angulo += self.velocidade_angular * dt
        self.t0_morte = now

        # Realizando a movimentação vertical:
        dt_mov = (now - self.t0_morte_movimentacao) / 1000
        self.rect.y += self.velocidade_y * dt_mov
        self.t0_morte_movimentacao = now

        # Realizando a inversão do movimento angular:
        if self.angulo > 45:
            self.velocidade_angular = -abs(self.velocidade_angular)
        elif self.angulo < -45:
            self.velocidade_angular = abs(self.velocidade_angular)
        
        # Realizando a animação:
        centro = self.rect.center
        self.image = pygame.transform.rotate(IMAGEM_CASCA_OVO, self.angulo)
        self.rect = self.image.get_rect(center=centro)
    
    def update(self) -> None:
        """
        Atualiza o estado da Plataforma.

        Returns:
            None:
        """

        # Realiza a movimentação da plataforma:
        if self.vivo:
            self.movimentar()
        else:
            self.movimentar_morte()

        # Mudando o estado de vivo quando morrer:
        if self.tweedle_dum.vidas <= 0 and self.vivo:
            self.t0_morte = self.t0_morte_movimentacao = pygame.time.get_ticks()
            self.vivo = False
        
        # Dando kill quando excede os limites:
        if self.rect.top > ALTURA_TELA:
            self.kill()

        # Atualiza o mask da plataforma:
        self.mask = pygame.mask.from_surface(self.image)
