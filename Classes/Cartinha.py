# 1. Módulos da biblioteca padrão
from math import sqrt, atan, degrees
from random import randint

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaCopas import AliceRainhaCopas

class Cartinha(pygame.sprite.Sprite):
    """
    Representa as Classes das Cartinhas da Rainha de Copas.

    Attributes:
        t_0 (int): O tempo em que a Tela é iniciada.
        imagem (Surface): Imagem inicial da Cartinha (usada para evitar transformações acumuladas).
        image (Surface): Imagem inicial da Cartinha.
        mask (Mask): Mask inicial da Cartinha.
        pos_x (int): Posição inicial horizontal randomizada da Cartinha.
        pos_y (int): Posição inicial verticial randomizada da Cartinha.
        velocidade_x (int): Velocidade horizontal inicial randomizada a Cartinha.
        velocidade_y (int): Velocidade vertical inicial randomizada a Cartinha.
        aceleracao (int): Módulo da aceleração da Cartinha.
        alice (AliceRainhaCopas): Instância de AliceRainhaCopas.
        angulo (float): Ângulo em relação à horizontal que a Cartinha se move.
        vivo (str): Estado atual da carta: "Vivo", "Morrendo" ou "Morto".
        t0_morte (int): O tempo em que a Cartinha morre.
        rect (Rect): Rect inicial da Cartinha.
        delta_t_acel (int): Intervalo de tempo entre a geração de cartinhas que aceleram.
    """
    
    def __init__(self, alice : AliceRainhaCopas) -> None:
        """
        Inicializa uma instância da classe cartinha.

        Args:
            alice (AliceRainhaCopas): Personagem Alice que enfrenta a Rainha de Copas.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.t0 = pygame.time.get_ticks()
        self.imagem = self.image = LISTA_IMAGENS_CARTINHA[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_x = LARGURA_TELA - 200 + randint(-150, 50)
        self.pos_y = ALTURA_TELA + randint(-300, -100)
        self.velocidade_x = randint(-80, -10)
        self.velocidade_y = randint(-50, -10)
        self.aceleracao = 30
        self.alice = alice
        self.angulo = 0.0 
        self.vivo = "Vivo"
        self.t0_morte = 0
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.delta_t_acel = 5000

    def movimentar_acelerando(self) -> None:
        """
        Movimenta a Cartinha seguindo um alvo -> Curva de Perseguição (modelo matemático).

        Returns:
            None
        """

        # Projeto futuro: usar coordenadas polares para melhorar o movimento da cartinha, pois a curva de perseguição não é tão precisa.

        # Encontrando as distâncias entre o alvo e a cartinha:
        self.alvo_x = self.alice.rect.centerx
        self.alvo_y = self.alice.rect.centery

        self.delta_x = self.alvo_x - self.rect.centerx
        self.delta_y = self.alvo_y - self.rect.centery

        # O try é necessário, pois se o delta_x == delta_y == 0, daria ZeroDivisionError:
        try:
            self.aceleracao_x = ((self.delta_x)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao 
            self.aceleracao_y = ((self.delta_y)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao
        except ZeroDivisionError:
            self.aceleracao_x = 0
            self.aceleracao_y = 0

        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        # Processo de aceleração, o qual altera a velocidade das cartinhas:
        self.velocidade_x += self.aceleracao_x * self.delta_t * 1.5
        self.velocidade_y += self.aceleracao_y * self.delta_t * 1.5

        # Movimenta horizontalmente a cartinha nos limites do mapa:
        if 20 <= self.rect.left and self.rect.right <= LARGURA_TELA - 20:
            self.rect.x += self.velocidade_x * self.delta_t
        elif self.rect.left < 20:
            self.rect.left = 20
            self.velocidade_x = 0
        elif self.rect.right > LARGURA_TELA - 20:
            self.rect.x = LARGURA_TELA - 20
            self.velocidade_x = 0

        # Movimenta verticalmente a cartinha nos limites do mapa:
        if 10 <= self.rect.top and self.rect.bottom <= ALTURA_TELA - 65:
            self.rect.y += self.velocidade_y * self.delta_t
        elif self.rect.top < 10:
            self.rect.top = 10
            self.velocidade_y = 0
        elif self.rect.bottom > ALTURA_TELA - 65:
            self.rect.bottom = ALTURA_TELA - 65
            self.velocidade_y = 0

        self.t0 = self.t1

    def animar(self) -> None:
        """
        Realiza as animações das Cartinhas batendo asa.

        Returns:
            None:
        """

        # Animando o bater das asas das cartinhas:
        dt = (pygame.time.get_ticks() - self.t0) % 500
        indice = dt // 250
        self.imagem = LISTA_IMAGENS_CARTINHA[indice]

    def rotacionar(self) -> None:
        """
        Rotaciona as imagens de acordo com o ângulo de velocidade da Cartinha.

        Returns:
            None:
        """

        # Rotacionando a cartinha, a fim de parecer que ela se move em direção ao jogador:
        self.alvo_x = self.alice.rect.centerx
        self.alvo_y = self.alice.rect.centery
        self.delta_x = self.alvo_x - self.rect.centerx
        self.delta_y = self.alvo_y - self.rect.centery

        # O try é necessário, pois a velocidade_x pode ser 0.
        try:
            theta = degrees(atan(abs(self.velocidade_y/self.velocidade_x)))
            if self.velocidade_y < 0:
                if self.velocidade_x < 0:
                    self.angulo = 90 - theta
                else:
                    self.angulo = theta - 90
            else:
                if self.velocidade_x < 0:
                    self.angulo = 90 + theta
                else:
                    self.angulo = - theta - 90
        except:
            self.angulo = 0
        
        antigo_centro = self.rect.center
        self.image = pygame.transform.rotate(self.imagem, self.angulo)
        self.rect = self.image.get_rect(center = antigo_centro)
    
    def animar_morte(self) -> None:
        """
        Realiza a animação de morte da cartinha, a qual ocorre quando a cartinha tem self.vivo == "Morrendo".

        Returns:
            None:
        """
        
        # Realizando a animação da morte de uma cartinha:
        dt = (pygame.time.get_ticks() - self.t0_morte) %  2800
        indice = dt // 400

        # Seleciona a imagem de acordo com o índice. Além disso, quando ele é maior do que 5, muda-se o estado para Morto.
        try:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[indice]
        except IndexError:
            self.vivo = "Morto"
        
        # Rotaciona a imagem de acordo com o ângulo da velocidade logo antes de morrer:
        centro = self.rect.center
        self.image = pygame.transform.rotate(self.imagem, self.angulo)
        self.rect = self.image.get_rect(center=centro)
    
    def update(self) -> None:
        """
        Atualiza o estado da Cartinha.

        Returns:
            None:
        """

        # Anima a Cartinha de acordo com o estado do self.vivo:
        if self.vivo == "Vivo":
            self.animar()
        elif self.vivo == "Morrendo":
            self.animar_morte()
        elif self.vivo == "Morto":
            self.kill()

        # Rotaciona a imagem da Cartinha de acordo com o ângulo:
        self.rotacionar()

        # Atualiza a mask da Cartinha:
        self.mask = pygame.mask.from_surface(self.image)