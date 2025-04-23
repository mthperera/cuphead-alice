# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaVermelha import AliceRainhaVermelha
from Classes.Livro import Livro

class RainhaVermelha(pygame.sprite.Sprite):
    """
    Representa a Rainha vermelha, a qual representa o chefão da fase 3.

    Attributes:
        pos_x (int): Posição horizontal da Rainha Vermelha.
        pos_y (int): Posição vertical inicial da Rainha Vermelha.
        alice (AliceRainhaVermelha): Instância da personagem AliceRainhaVermelha
        t0_livro (int): O tempo em que o livro é lançado.
        t0 (int): O tempo em que a Rainha Vermelha é criada.
        image (Surface): Imagem inicial da Rainha Vermelha.
        mask (Mask): Mask inicial da Rainha vermelha.
        grupo_livros (Group): Grupo de sprites dos livros lançados pela Rainha.
        vidas (int): Vidas totais da Rainha vermelha.
    """

    def __init__(self, x : int, y : int, alice : AliceRainhaVermelha) -> None:
        """
        Inicializa instância da classe RainhaVermelha.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.alice = alice
        self.t0_livro = self.t0 = pygame.time.get_ticks()
        self.lancou_livro = False
        self.image = LISTA_RAINHA_VERMELHA[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_livros = pygame.sprite.Group()
        self.vidas = 20
    
    def jogar_livro(self) -> None:
        """
        Realiza a animação da Rainha Vermelha jogando livros.

        Returns:
            None:
        """

        # Realizando aremesso de livos a cada certo período em ms:
        self.t1 = pygame.time.get_ticks()

        dt = (self.t1 - self.t0_livro) % 3200
        indice = dt // 800
        self.image = LISTA_RAINHA_VERMELHA[indice]

        if indice == 2:
            self.lancou_livro = False
        if indice == 3:
            if not self.lancou_livro:
                self.grupo_livros.add(Livro(LARGURA_TELA - 200, 105, self.alice))
                self.lancou_livro = True
        
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
        Atualiza a Rainhavermelha.

        Returns:
            None
        """
        
        # Anima o lançar livros:
        self.jogar_livro()

        # Movimenta a Rainha
        self.movimentar()

        # Dá kill na RainhaVermelha se a vida dela esgotar:
        if self.vidas <= 0:
            self.kill()
        
        # Atualiza a mask da RainhaVermelha.
        self.mask = pygame.mask.from_surface(self.image)