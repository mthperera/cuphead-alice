# 1. Módulos da biblioteca padrão
from math import cos
from random import randint

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaCopas import AliceRainhaCopas
from Classes.Cartinha import Cartinha
from Classes.Coracao import Coracao

class RainhaCopas(pygame.sprite.Sprite):
    """
    Representa a Rainha de Copas, a qual representa o chefão da fase 1.

    Attributes:
        alice (AliceRainhaCopas): Instância de AliceRainhaCopas.
        grupo_cartinhas (Group): Grupo das sprites Cartinhas.
        grupo_coracoes (Group): Grupo das sprites Coracoes.
        t0_movimento (int): O tempo em que o movimento é iniciado.
        t0 (int): O tempo em que a Rainha de Copas é criada.
        pos_x (int): Posição horizontal inicial da Rainha de Copas.
        pos_y (int): Posição vertical inicial da Rainha de Copas.
        image (Surface): Representa a imagem inicial da Rainha de Copas.
        mask (Mask): Mask inicial da Rainha de Copas.
        rect (Rect): Rect inicial da Rainha de Copas.
        ataque_coracao (str): String que indica se a Rainhde Copas está atacando com corações ou não.
        t0_ataque (int): O tempo em que o ataque de corações começou.
        delta_t_remove (int): Intervalo de tempo para remover as cartinhas.
        delta_t_acel (int): Intervalo de tempo para gerar cartinhas que aceleram.
        delta_t_coracao (int): Intervalo de tempo para gerar corações.
        vidas (int): Vidas totais da Rainha de Copas.

    """

    def __init__(self, alice : AliceRainhaCopas) -> None:
        """
        Inicializa uma instância da classe Rainha de Copas.

        Returns:
            None:
        """
        self.alice = alice
        pygame.sprite.Sprite.__init__(self)
        self.grupo_cartinhas = pygame.sprite.Group()
        self.grupo_coracoes = pygame.sprite.Group()
        self.t0_movimento = self.t0 = pygame.time.get_ticks()
        self.pos_x = LARGURA_TELA - 350
        self.pos_y = ALTURA_TELA - 440
        self.image = LISTA_INVOCAR_CORACAO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom=(self.pos_x, self.pos_y))
        self.ataque_coracao = "Sem ataque"
        self.t0_ataque = 0
        self.delta_t_remove = 15000
        self.delta_t_acel = 5000
        self.delta_t_coracao = 5000
        self.vidas = 30
    
    def invocar_coracoes(self) -> None:
        """
        Faz a animação da invocação dos corações.

        Returns:
            None:
        """

        # Animação de invocar corações:
        dt = (pygame.time.get_ticks() - self.t0_ataque) %  6000
        indice = dt // 6000
        indice = 4 - indice if indice > 4 else indice
        if indice >= 0:
            self.image = LISTA_INVOCAR_CORACAO[indice]
        else:
            self.image = LISTA_INVOCAR_CORACAO[0]
            self.ataque_coracao = "Sem ataque"

    def movimentar(self) -> None:
        """
        Movimenta o Ioiô numa figura diferente matematicamente: Figura de Lissajous.

        Returns:
            None:
        """

        # Ioio fazendo uma Figura de Lissajous por meio de dois MHS ortogonais.
        # Isso foi feito para dar uma sensação de movimento mais real.
        self.rect.x = self.pos_x + 50*cos(1*(pygame.time.get_ticks()-self.t0_movimento)/1000)
        self.rect.y = self.pos_y + 3*cos(2*(pygame.time.get_ticks()-self.t0_movimento)/1000)

    def update(self) -> None:
        """
        Atualiza a Rainha de Copas.

        Returns:
            None:
        """

        # Spawnando cartinhas a cada self.delta_t_acel ms:
        if (pygame.time.get_ticks() - self.t0) // self.delta_t_acel > 0 and (pygame.time.get_ticks()- self.t0) < 100000:
            for _ in range(randint(5, 7)):
                cartinha = Cartinha(self.alice)
                self.grupo_cartinhas.add(cartinha)

            self.delta_t_acel += 5000
        
        # Spawnando coracoes a cada self.delta_t_coracao ms:
        if (pygame.time.get_ticks() - self.t0 - 30000) // self.delta_t_coracao > 0:
            self.ataque_coracao = "Atacando"
            for _ in range(randint(5, 7)):
                coracao = Coracao()
                self.grupo_coracoes.add(coracao)
                self.t0_ataque = pygame.time.get_ticks()

            self.delta_t_coracao += 6000
        
        # Matando cartinhas em excesso:
        if (pygame.time.get_ticks() - self.t0) // self.delta_t_remove > 0 and (pygame.time.get_ticks() - self.t0) < 100000:
            if len(self.grupo_cartinhas) > 3:
                i=0
                for cartinha in self.grupo_cartinhas:
                    if i > 3:
                        break
                    cartinha.vivo = "Morrendo"
                    cartinha.t0_morte = pygame.time.get_ticks()
                    i += 1

                    self.delta_t_remove += 10000

        # Movimenta a Rainha de Copas (Figura de Lissajous):
        self.movimentar()

        # Invoca os corações:
        if self.ataque_coracao == "Atacando":
                self.invocar_coracoes()
        
        # Atualiza a mask da Rainha de Copas:
        self.mask = pygame.mask.from_surface(self.image)