# 1. Módulos da biblioteca padrão
from math import cos, atan2, degrees

# 2. Módulos de terceiros (pip)
import pygame
from pygame.event import Event

# 3. Módulos locais
from constantes import *
from Classes.Bolinho import Bolinho

class AliceRainhaVermelha(pygame.sprite.Sprite):
    """
    Personagem Alice da fase 3: Rainha Vermelha.

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
        t0_andar (int): Tempo em que a animação de andar iniciou.
        t0_caindo (int): Tempo em que a ação de cair da plataforma começou.  
        velocidade_x (int): Velocidade horizontal da Alice.
        atacou_bolinho (bool): Indica se de fato já atacou o bolinho.
        atacando_bolinho (bool): Indica se está no movimento de atacar o bolinho.
        atacou_superbolo (bool): Indica se de fato já atacou o superbolo.
        atacando_superbolo (bool): Indica se está no movimento de atacar o superbolo.
        andando (bool): Indica se está durante o movimento de andar.
        caindo (bool): Indica se está durante o movimento de cair da plataforma.
        direcao (str): Indica se está se movendo para a Esquerda ou para a Direita.
        angulo (float): Indica qual o ângulo exercido pelo analógico esquerdo.
        t0_ultimo_dano (int): Indica o tempo em que a Alice tomou o último dano.
        canal_pulo (Channel): Canal utilizado para o som de pulo.
        canal_atacando (Channel): Canal utilizado para o som da Alice atacando.
    """

    def __init__(self, x : int, y : int) -> None:
        """
        Inicializa a instância da classe AliceRainhaVermelha.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.pos_y_inicial = self.pos_y
        self.vidas = 5
        self.image = LISTA_ALICE_SUPER_BOLO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom = (self.pos_x, self.pos_y))
        self.grupo_bolinhos = pygame.sprite.Group()
        self.t0 = pygame.time.get_ticks()
        self.t0_bolinho = self.t0_atacou_bolinho = pygame.time.get_ticks()
        self.t0_superbolo = self.t0_atacou_superbolo = pygame.time.get_ticks()
        self.t0_andar = self.t0_caindo = pygame.time.get_ticks()
        self.velocidade_x = 100
        self.atacou_bolinho = self.atacando_bolinho = False
        self.atacou_superbolo = self.atacando_superbolo = False
        self.andando = self.caindo = False
        self.direcao = None
        self.angulo = 0
        self.t0_ultimo_dano = pygame.time.get_ticks()
        self.canal_pulo = pygame.mixer.Channel(1)
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
        if indice >= 4 and not self.atacou_bolinho:
            if not self.atacou_bolinho:
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho + 15))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho - 15))
                self.atacou_bolinho = True
        elif indice > 10:
            self.image = LISTA_ALICE_SUPER_BOLO[0]
            self.atacando_bolinho = False
            self.atacou_bolinho = False
            self.angulo_bolinho = 0
            if not self.atacando_bolinho and not self.atacando_superbolo:
                if hasattr(self, 'value_0') and abs(self.value_0) > 0.5:
                    self.direcao = "Direita" if self.value_0 > 0 else "Esquerda"
                    if not self.andando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.andando = True
                else:
                    self.andando = False
                    self.direcao = None
        else:
            self.image = LISTA_ALICE_BOLINHO[indice]
        
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
            self.image = LISTA_ALICE_SUPER_BOLO[indice]

    def andar(self, direcao : str) -> None:
        """
        Movimenta a personagem Alice e troca as imagens (animação):

        Args:
            direcao (str): String que representa a direção do movimento: Direita ou Esquerda.

        Returns:
            None:
        """

        # Realiza a movimentação da Alice:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_andar_movimentacao) / 1000

        if direcao == "Direita":
            self.rect.x += self.velocidade_x * dt
        elif direcao == "Esquerda":
            self.rect.x -= self.velocidade_x * dt

        self.t0_andar_movimentacao = now
        
        # Realiza a animação da personagem andando:
        delta_t = (pygame.time.get_ticks() - self.t0_andar_animacao) % (70*18)
        indice = delta_t // 70
        self.image = LISTA_ALICE_CORRENDO[indice]

        antigo_centro = self.rect.center
        if direcao == "Direita":
            self.image = pygame.transform.flip(self.image, True, False)
        
        elif direcao == "Esquerda":
            pass
        self.rect = self.image.get_rect(center = antigo_centro)

    def movimentar_plataforma(self) -> None:
        """
        Movimenta verticalmente em MHS, seguindo a Plataforma de Xadrez.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.pos_y = self.pos_y_inicial + 10 * cos((pygame.time.get_ticks() - self.t0)/1000)
        self.rect.y = self.pos_y
    
    def cair(self) -> None:
        """
        Realiza a movimentação de cair da Plataforma de Xadrez:

        Returns:
            None:
        """

        # Realiza movimento de queda simples em movimento uniforme:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_caindo)/1000

        self.rect.y += 200 * dt

        self.t0_caindo = now
    
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

                # Iniciando movimentação de andar:
                if evento.axis == 0:
                    if not self.andando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.andando = True
                    if evento.value > 0.5:
                        self.direcao = "Direita"
                    elif evento.value < -0.5:
                        self.direcao = "Esquerda"
                    else:
                        self.direcao = None
                        self.andando = False
                    self.value_0 = evento.value
                elif evento.axis == 1:
                    self.value_1 = evento.value

                # Aqui o try é necessário, pois pode ser que o value_1 ou o value_0 não exista.
                try:
                    self.angulo = (degrees(atan2(-self.value_1, self.value_0)) + 360) % 360
                except AttributeError:
                    self.angulo = 90 if not hasattr(self, 'value_0') else 0


            if evento.type == pygame.JOYBUTTONDOWN:

                # Inicando ataque bolinho:
                if evento.button == 2 and pygame.time.get_ticks() - self.t0_atacou_bolinho > 2000:
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

            # Iniciando movimentação de correr:
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade_x = 200
                    else:
                        self.velocidade_x = 150

        # Realizando animação e execução do ataque bolinho:
        if self.atacando_bolinho:
            self.andando = False
            self.ataque_bolinho()
        
        # Realizando animação e execução do ataque superbolo:
        if self.atacando_superbolo:
            self.super_bolo()
        
        # Realizando movimentação e animação do andar dentro dos limites da Plataforma de Xadrez:
        if self.andando:
            if LARGURA_TELA//2 - 3.5*ALTURA_TELA//8 + 50 < self.rect.centerx < LARGURA_TELA//2 + 3.5*ALTURA_TELA//8 + 15:
                self.andar(self.direcao)

        # Faz a Alice cair caso ela esteja fora da Plataforma de Xadrez:
        if self.rect.centerx > 3.5*ALTURA_TELA//8 + LARGURA_TELA//2 or self.rect.centerx < - 3.5*ALTURA_TELA//8 + 65 + LARGURA_TELA//2:
            if not self.caindo:
                self.t0_caindo = pygame.time.get_ticks()
                self.caindo = True
            self.cair()
        else:
            self.movimentar_plataforma()

        # Implementando imagem base caso não esteja executando nenhuma ação:
        if not (self.andando or self.atacando_bolinho or self.atacando_superbolo):
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        
        # Mata a Alice assim que ela sai da tela (quando ela cai da Plataforma de Xadrez):
        if self.rect.top > ALTURA_TELA:
            self.vidas = 0

        # Diminui o tamanho da Alice e atualiza o mask:
        self.image = pygame.transform.scale(self.image, (128, 192))
        self.mask = pygame.mask.from_surface(self.image)