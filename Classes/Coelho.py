# 1. Módulos da biblioteca padrão
from math import sqrt, atan, degrees

# 2. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 3. Módulos locais
from constantes import *

class Coelho:
    """
    Representa o Coelho da Alice, o qual pula no buraco e dá início à história:

    Attributes:
        pos_x (int): Posição horizontal inicial do Coelho.
        pos_y (int): Posição vertical inicial do Coelho (mutável e usada para movimentar o coelho).
        pos_y_inicial (int): Posição verticial inicial do Coelho (imutável e usada para fazer comparações).
        image (Surface): Imagem inicial do Coelho.
        pulo (bool): Booleano que diz se o coelho está pulando ou não.
        velocidade_x (int): Velocidade horizontal do Coelho antes do pulo.
        velocidade_x_fim (int): Velocidade horizontal do Coelho durante o pulo.
        velocidade_y (int): Velocidade inicial vertical do Coelho no pulo.
        aceleracao_y (int): Aceleração "gravitacional".
    """
    
    # Essa classe não está herdando o pygame.sprite.Sprite(), pois não é uma entidade, mas, sim, uma animação!

    def __init__(self) -> None:
        """
        Inicializa uma instância da classe Coelho.

        Returns:
            None:
        """
        self.pos_x = 20
        self.pos_y_inicial = self.pos_y = ALTURA_TELA - 275 - (170-128)
        self.t0 = self.t0_inicio = self.t0_pulo = pygame.time.get_ticks()
        self.image = LISTA_COELHO_CORRENDO[0]
        self.pulo = False
        self.velocidade_x = 300
        self.velocidade_x_fim = 700
        self.velocidade_y = -500
        self.aceleracao_y = 1000

    def movimentar(self) -> None:
        """
        Realiza a movimentação horizontal do coelho antes do pulo.

        Returns:
            None:
        """

        # Movimentação simples sem aceleração:
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.pos_x += self.velocidade_x * self.dt

        self.t0 = self.t1
    
    def animar(self) -> None:
        """
        Realiza a animação do coelho correndo (movimentando as perninhas):

        Returns:
            None:
        """

        # Animação do coelho correndo:
        dt = (pygame.time.get_ticks() - self.t0_inicio) % 500
        indice = dt // 250
        self.image = LISTA_COELHO_CORRENDO[indice]

    def pular(self) -> None:
        """
        Realiza a movimentação vertcial do coelho (pulinhos).

        Returns:
            None:
        """

        # Animação do coelho pulando e desaparecendo posteriormente:
        self.t1 = pygame.time.get_ticks()
        self.dt_pulo = (self.t1 - self.t0_pulo)/1000

        # Alterando a velocidade do coelho de acordo com a aceleração:
        self.velocidade_y += self.aceleracao_y * self.dt_pulo
        self.pos_y += self.velocidade_y * self.dt_pulo

        if self.pos_y > self.pos_y_inicial - 30:
            self.velocidade_x = self.velocidade_x_fim
            # Diminuindo a opacidade da imagem do coelho:
            self.image.set_alpha(255- self.i*50)
            self.i += 1
        else:
            self.image = LISTA_COELHO_PULANDO[0]
            self.angulo = degrees(atan(self.velocidade_x/sqrt(self.velocidade_x**2 + self.velocidade_y**2)))
            self.image = pygame.transform.rotate(self.image, self.angulo)
        
        # Fazendo ele parar de se movimentar após sair da tela:
        if self.rect.top > LARGURA_TELA:
            self.rect.top = LARGURA_TELA
            self.velocidade_y = 0
            self.aceleracao_y = 0

        self.t0_pulo = self.t1

    def desenhar(self, window : Surface) -> None:
        """
        Desenha o coelho na tela.

        Returns:
            None:
        """

        # Desenha o coelho na tela de acordo com as suas posições:
        window.blit(self.image, (self.pos_x, self.pos_y))



