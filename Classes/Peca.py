# 1. Módulos da biblioteca padrão
from random import choice, randint

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class Peca(pygame.sprite.Sprite):
    """
    Representa as peças de xadrez que o Rei vermelho invoca e caem sobre a Alice.

    Attributes:
        pos_x (int): Posição horizontal randomizada inicial das peças.
        pos_y (int): Posição vertical randomizada inicial das peças.
        velocidade_y (int): Velocidade vertical em que as peças se mexem para baixo.
        t0 (int): O tempo em que a Peça é criada (invocada) pelo Rei Vermelho.
        image (Surface): Imagem da peça randomizada, a qual pode ser: Peão, Torre, Cavalo ou Bispo.
        mask (Mask): Mask inicial da Peça.
        rect (Rect): Rect inicial da Peça.
    """

    def __init__(self) -> None:
        """
        Inicializa uma instância da classe Peça.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = randint(230, LARGURA_TELA - 230)
        self.pos_y = randint(-400, -50)
        self.velocidade_y = 300
        self.t0 = pygame.time.get_ticks()
        self.image = choice(LISTA_PECAS)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self) -> None:
        """
        Movimenta a Peça retilinea e verticalmente caindo.

        Returns:
            None:
        """

        # Movimento de queda simples, por meio de movimento retilíneo uniforme.
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1

    def update(self) -> None:
        """
        Atualiza a peça de xadrez.

        Returns:
            None:
        """

        # Movimenta a peça caindo:
        self.movimentar()
        
        # Dando kill nas peças que excedem os limites do mapa:
        if self.rect.top > ALTURA_TELA:
            self.kill()
        elif self.rect.right < 0 or self.rect.left > LARGURA_TELA:
            self.kill()
        
        # Atualizando o mask da peça:
        self.mask = pygame.mask.from_surface(self.image)