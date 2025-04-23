# 1. Módulos da biblioteca padrão
from random import randint

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class Coracao(pygame.sprite.Sprite):
    """
    Representa o coração (copas) invocado pela Rainha de Copas.

    Attributes:
        t0 (int): O tempo em que a Tela é iniciada.
        t0_animar (int): Tempo que inicia a animação do coração (quando é gerado).
        t0_morte (int): Tempo que inicia a animação da morte (quando é atingido).
        image (Surface): Imagem inicial do coração.
        mask (Mask): Mask inicial do coração.
        pos_x (int): Posição inicial horizontal randomizada do coração.
        pos_y (int): Posição inicial verticial randomizada do coração.
        velocidade_y (int): Velocidade vertical que os corações caem.
        vivo (str): String que representa o estado da carta, o qual pode ser "Vivo", "Morrendo" ou "Morto".
        rect (Rect): Rect inicial do coração.

    """
    
    def __init__(self) -> None:
        """
        Inicializa uma instância da classe Coração.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.t0 = self.t0_animar = pygame.time.get_ticks()
        self.t0_morte = 0
        self.image = LISTA_CORACAO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_x = randint(50, LARGURA_TELA - 200)
        self.pos_y = randint(-1000, -500)
        self.velocidade_y = 200
        self.vivo = "Vivo"
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def movimentar(self) -> None:
        """
        Movimenta as cartinhas para baixo.

        Returns:
            None:
        """

        # Movimentação retilínea simples vertical:
        now = pygame.time.get_ticks()
        self.delta_t = (now - self.t0)/1000

        self.rect.y += self.velocidade_y * self.delta_t

        self.t0 = now
    
    def animar(self) -> None:
        """
        Realiza a animação dos corações piscando.

        Returns:
            None:
        """

        dt = (pygame.time.get_ticks() - self.t0_animar) % 1200
        indice = dt // 800
        self.image = LISTA_CORACAO[indice] 

    def animar_morte(self) -> None:
        """
        Realiza animação da morte do coração, o qual ocorre no estado self.vivo == "Morrendo".

        Returns:
            None
        """

        # Animando a morte, de modo a dar um efeito de coração quebrando:
        dt = (pygame.time.get_ticks() - self.t0_morte) %  1750
        indice = dt // 250

        # Seleciona a imagem de acordo com o índice. Além disso, quando ele é maior do que 5, muda-se o estado para Morto.
        try:
            self.image = LISTA_EXPLOSAO_CORACAO[indice]
        except IndexError:
            self.vivo = "Morto"

    def update(self) -> None:
        """
        Atualiza o estado do Coração.

        Returns:
            None:
        """
        
        # Anima o Coraão de acordo com o estado do self.vivo:
        if self.vivo == "Vivo":
            self.movimentar()
            self.animar()
        if self.rect.bottom >= ALTURA_TELA and self.vivo == "Vivo":
            self.t0_morte = pygame.time.get_ticks()
            self.vivo = "Morrendo"
        if self.vivo == "Morrendo":
            self.animar_morte()
        if self.vivo == "Morto":
            self.kill()
        
        # Atualiza o mask do Coração:
        self.mask = pygame.mask.from_surface(self.image)