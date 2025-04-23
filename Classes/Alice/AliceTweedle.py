# 1. Módulos da biblioteca padrão
from math import cos, sin, atan2, degrees, radians

# 2. Módulos de terceiros (pip)
import pygame
from pygame.event import Event

# 3. Módulos locais
from constantes import *
from Classes.Bolinho import Bolinho


class AliceTweedle(pygame.sprite.Sprite):
    """
    Personagem Alice da fase 2: Irmãos Tweedle.

    Attributes:
        pos_x (int): Posição horizontal inicial da Alice.
        pos_y (int): Posição vertical inicial da Alice.
        vidas (int): Vidas totais da Alice.
        image (Surface): Imagem inicial da Alice.
        mask (Mask): Mask inicial da Alice.
        rect (Rect): Rect inicial da Alice.
        grupo_bolinhos (Group): Grupo de sprites dos bolinhos.
        t0 (int): O tempo em que a Alice foi criada.
        t0_bolinho (int): Tempo em que a animação de atacar bolinho começou.
        t0_atacou_bolinho (int): Tempo em que o bolinho de fato foi atacado.
        t0_superbolo (int): Tempo em que a animação de atacar superbolo começou.
        t0_atacou_superbolo (int): Tempo em que o superbolo de fato foi atacado.
        t0_voar_movimentacao (int): Tempo em que a movimentação de voar iniciou.
        t0_voar_animacao (int): Tempo em que a animação de voar iniciou.
        velocidade (int): Velocidade da Alice.
        atacou_bolinho (bool): Indica se de fato já atacou o bolinho.
        atacando_bolinho (bool): Indica se está no movimento de atacar o bolinho.
        atacou_superbolo (bool): Indica se de fato já atacou o superbolo.
        atacando_superbolo (bool): Indica se está no movimento de atacar o superbolo.
        voando (bool): Indica se está durante o movimento de voar.
        direcao (str): Indica se está se movendo para a Esquerda ou para a Direita.
        angulo (float): Indica qual o ângulo exercido pelo analógico esquerdo.
        t0_ultimo_dano (int): Indica o tempo em que a Alice tomou o último dano.
        canal_atacando (Channel): Canal utilizado para o som da Alice atacando.
    """
    
    def __init__(self, x : int, y : int) -> None:
        """
        Inicializa a instância da classe AliceTweedle.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.vidas = 5
        self.image = LISTA_ALICE_AVIAO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        self.grupo_bolinhos = pygame.sprite.Group()
        self.t0 = pygame.time.get_ticks()
        self.t0_bolinho = self.t0_atacou_bolinho = pygame.time.get_ticks()
        self.t0_superbolo = self.t0_atacou_superbolo = pygame.time.get_ticks()
        self.t0_voar_movimentacao = self.t0_voar_animacao = pygame.time.get_ticks()
        self.velocidade = 300
        self.atacou_bolinho = self.atacando_bolinho = False
        self.atacou_superbolo = self.atacando_superbolo = False
        self.voando = False
        self.direcao = None
        self.angulo = 0
        self.t0_ultimo_dano = pygame.time.get_ticks()
        self.canal_atacando = pygame.mixer.Channel(2)

    def ataque_bolinho(self) -> None:
        """
        Realiza a animação do ataque dos bolinhos e invoca os bolinhos.

        Returns:
            None:
        """

        # Invoca os bolinhos a cada período e altera as imagens da animação:
        delta_t = pygame.time.get_ticks() - self.t0_bolinho
        indice = delta_t // 20
        if indice >= 2 and not self.atacou_bolinho:
            if not self.atacou_bolinho:
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho + 15))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho - 15))
                self.atacou_bolinho = True
        elif indice > 10:
            self.image = LISTA_ALICE_AVIAO[0]
            self.atacando_bolinho = False
            self.atacou_bolinho = False
            self.angulo_bolinho = 0
            if not self.atacando_bolinho and not self.atacando_superbolo:
                if hasattr(self, 'value_0') and abs(self.value_0) > 0.5:
                    self.direcao = "Direita" if self.value_0 > 0 else "Esquerda"
                    if not self.voando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.voando = True
                else:
                    self.voando = False
                    self.direcao = None
        else:
            self.image = LISTA_ALICE_AVIAO[indice]
        
        # Inverte a imagem (flip) caso o angulo de lançamento seja diferente da imagem origal:
        if 0 <= self.angulo_bolinho <= 90 or 270 <= self.angulo_bolinho <= 360:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center = antigo_centro)

    def super_bolo(self) -> None:
        """
        Realiza a animação do ataque do superbolo e invoca os bolinhos.

        Returns:
            None:
        """

        # Invoca os bolinhos a cada período e altera as imagens da animação:
        delta_t = pygame.time.get_ticks() - self.t0_superbolo
        indice = delta_t // 50
        if indice >= 7 and not self.atacou_superbolo:
            if not self.atacou_superbolo:
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 0))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 30))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 60))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 90))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 120))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 150))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 180))
                self.atacou_superbolo = True
        if indice > 10:
            self.atacando_superbolo = False
            self.atacou_superbolo = False
        
        else:
            self.image = LISTA_ALICE_AVIAO[indice]

    def voar_movimentacao(self, angulo : float) -> None:
        """
        Realiza a movimentação da Alice voar de acordo com o ângulo do analógico esquerdo.

        Returns:
            None:
        """

        # Realiza a movimentação de voar:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_voar_movimentacao) / 1000

        velocidade_x = self.velocidade * cos(radians(angulo))
        velocidade_y = self.velocidade * sin(radians(angulo))

        self.rect.x += velocidade_x * dt
        self.rect.y -= velocidade_y * dt

        self.t0_voar_movimentacao = now
        
    def voar_animacao(self, direcao : str) -> None:
        """
        Realiza a animação da Alice voar.
        """

        # Define a imagem usada na animação do voar:
        delta_t = (pygame.time.get_ticks() - self.t0_voar_animacao) % (200*13)
        indice = delta_t // 200
        self.image = LISTA_ALICE_AVIAO[indice]

        antigo_centro = self.rect.center

        # Inverte (flip) a imagem original de acordo com a direção do movimento:
        if direcao == "Direita":
            self.image = pygame.transform.flip(self.image, True, False)
        elif direcao == "Esquerda":
            pass

        self.rect = self.image.get_rect(center = antigo_centro)

    def update(self, lista_eventos : list[Event]) -> None:
        """
        Atualiza a AliceRainhaCopas, tais como os eventos do joystick, as animações e os movimentos.

        Args:
            lista_eventos (list[Event]): Lista de eventos capturadas pelo pygame.event.get() na tela.
        
        Returns:
            None:
        """

        # Analisa os eventos e associa às movimentações e animações, além de associar aos sons:
        for evento in lista_eventos:

            if evento.type == pygame.JOYAXISMOTION:

                # Iniciando movimentação de voar:
                if evento.axis in [0, 1]:
                    if not self.voando:
                        self.t0_voar_movimentacao = pygame.time.get_ticks()
                        self.voando = True
                    if evento.axis == 0:
                        if evento.value > 0.5:
                            self.direcao = "Direita"
                        elif evento.value < -0.5:
                            self.direcao = "Esquerda"
                        self.value_0 = evento.value
                    if evento.axis == 1:
                        self.value_1 = evento.value
                else:
                    self.voando = False

                # Aqui o try é necessário, pois pode ser que o value_1 ou o value_0 não exista.
                try:
                    if abs(self.value_0) < 0.2 and abs(self.value_1) < 0.2:
                        self.voando = False
                    else:
                        self.angulo = (degrees(atan2(-self.value_1, self.value_0)) + 360) % 360

                # As condições do except são adaptadas para desprezar pequenas angulações de resquícios no controle:
                except AttributeError:
                    self.angulo = 90 if not hasattr(self, 'value_0') else 0
                    if not hasattr(self, 'value_0') and not hasattr(self, 'value_1'):
                        self.voando = False
                    elif not hasattr(self, 'value_0') and self.value_1 < 0.2:
                        self.voando = False
                    elif not hasattr(self, 'value_1') and self.value_0 < 0.2:
                        self.voando = False

            if evento.type == pygame.JOYBUTTONDOWN:

                # Inicando ataque bolinho:
                if evento.button == 2 and pygame.time.get_ticks() - self.t0_atacou_bolinho > 1500:
                    self.atacando_bolinho = True
                    self.angulo_bolinho = self.angulo
                    self.t0_atacou_bolinho = self.t0_bolinho = pygame.time.get_ticks()
                    if not self.canal_atacando.get_busy():
                        self.canal_atacando.play(SOM_ALICE_ATACANDO, loops=0)

                # Iniciando ataque superbolo:
                if evento.button == 3 and pygame.time.get_ticks() - self.t0_atacou_superbolo > 4000:
                    self.atacando_superbolo = True
                    self.t0_atacou_superbolo = self.t0_superbolo = pygame.time.get_ticks()
                    if not self.canal_atacando.get_busy():
                        self.canal_atacando.play(SOM_ALICE_ATACANDO, loops=0)
            
            # Iniciando movimentação de voar mais rápido:
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade = 400
                    else:
                        self.velocidade = 300

        # Realizando a animação da Alice voando:
        self.voar_animacao(self.direcao)

        # Realizando animação e execução do ataque bolinho:
        if self.atacando_bolinho:
            self.ataque_bolinho()
        
        # Realizando animação e execução do ataque superbolo:
        if self.atacando_superbolo:
            self.super_bolo()
        
        # Realizando movimentação e animação de voar dentro dos limites do mapa:
        if self.voando:
            if self.rect.left >= 0 and self.rect.right <= LARGURA_TELA and self.rect.bottom <= ALTURA_TELA and self.rect.top >= 0:
                self.voar_movimentacao(self.angulo)
            elif self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA_TELA:
                self.rect.right = LARGURA_TELA
            elif self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > ALTURA_TELA:
                self.rect.bottom = ALTURA_TELA

        # Atualizando a mask da Alice:
        self.mask = pygame.mask.from_surface(self.image)