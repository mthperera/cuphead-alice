# 1. Módulos da biblioteca padrão
from math import atan2, degrees

# 2. Módulos de terceiros (pip)
import pygame
from pygame.event import Event

# 3. Módulos locais
from constantes import *

class AliceCoelho(pygame.sprite.Sprite):
    """
    Personagem Alice da primeira tela: Tela Coelho.

    Attributes:
        pos_x (int): Posição horizontal inicial da Alice.
        pos_y (int): Posição vertical inicial da Alice.
        image (Surface): Imagem inicial da Alice.
        mask (Mask): Mask inicial da Alice.
        rect (Rect): Rect inicial da Alice.
        t0 (int): O tempo em que a Alice foi criada.
        t0_andar (int): Tempo em que a animação de andar iniciou.
        t0_pular_animacao (int): Tempo em que a animação de pular começou.
        t0_pular_movimentacao (int): Tempo em que a movimentacao de pular começou.
        velocidade_x (int): Velocidade horizontal da Alice.
        velocidade_y (int): Velocidade inicial vertical da Alice (mutável).
        velocidade_y_inicial (int): Velocidade verticial da Alice (imutável - usada para comparações).
        aceleracao_y (int): Aceleração "gravitacional".
        andando (bool): Indica se está durante o movimento de andar.
        pulando (bool): Indica se está durante o movimento de pular.
        direcao (str): Indica se está se movendo para a Esquerda ou para a Direita.
        canal_pulo (Channel): Canal utilizado para o som de pulo.
    """

    def __init__(self, x : int, y : int) -> None:
        """
        Inicializa a instância da classe AliceCoelho.

        Returns:
            None:
        """
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.image = LISTA_ALICE_SUPER_BOLO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom = (self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
        self.t0_andar = pygame.time.get_ticks()
        self.t0_pular_animacao = self.t0_pular_movimentacao = pygame.time.get_ticks()
        self.velocidade_x = 100
        self.velocidade_y = self.velocidade_y_inicial = -500
        self.aceleracao_y = 1000
        self.andando = self.pulando = False
        self.direcao = None
        self.canal_pulo = pygame.mixer.Channel(1)
    
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

    def pular_movimentacao(self, direcao : str) -> None:
        """
        Movimenta a personagem Alice quando ela pula.

        Args:
            direcao (str): String que representa a direção do movimento: Direita ou Esquerda.

        Returns:
            None:
        """

        # Movimenta a Alice com um pulo:
        now = pygame.time.get_ticks()
        dt = (now - self.t0_pular_movimentacao) / 1000

        self.velocidade_y += self.aceleracao_y * dt
        self.rect.y += self.velocidade_y * dt
        if self.rect.bottom >= self.pos_y:
            self.rect.bottom = self.pos_y
            self.velocidade_y = self.velocidade_y_inicial
            self.pulando = False

        if self.rect.x > 0 and self.rect.x < LARGURA_TELA - 100:
            if direcao == "Direita":
                velocidade_x = abs(self.velocidade_x)
            elif direcao == "Esquerda":
                velocidade_x = -abs(self.velocidade_x)
            if direcao is not None:
                self.rect.x += velocidade_x * dt

        self.t0_pular_movimentacao = now

    def pular_animacao(self, direcao : str) -> None:
        """
        Realiza animação da Alice pulando.

        Args:
            direcao (str): String que representa a direção do movimento: Direita ou Esquerda.

        Returns:
            None:
        """

        # Movimenta a Alice com um pulo:
        delta_t = (pygame.time.get_ticks() - self.t0_pular_animacao) % (8*250)
        indice = delta_t // 250
        self.image = LISTA_ALICE_PULANDO[indice]
        
        if direcao == "Direita":
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center = antigo_centro)

    def update(self, lista_eventos : list[Event]) -> None:
        """
        Atualiza a AliceCoelho, tais como os eventos do joystick, as animações e os movimentos.

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

                # Iniciando pulo:
                if evento.button == 0:
                    if not self.pulando:
                        self.t0_pular_animacao = self.t0_pular_movimentacao = pygame.time.get_ticks()
                        self.rect.y -= 1
                        self.canal_pulo.play(SOM_ALICE_PULO, loops=0)
                    self.pulando = True
            
            # Iniciando movimentação de correr:
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade_x = 200
                    else:
                        self.velocidade_x = 150

        # Realizando animação do pulo:
        if self.pulando:
            self.andando = False
            self.pular_animacao(self.direcao)
        
        # Realizando movimentação e animação do andar dentro dos limites do mapa:
        if self.andando:
            self.pulando = False
            if self.rect.left >= 0 and self.rect.right <= LARGURA_TELA:
                self.andar(self.direcao)
            elif self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA_TELA:
                self.rect.right = LARGURA_TELA 
        
        # Implementando imagem base caso não esteja executando nenhuma ação:
        if not self.andando and not self.pulando:
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        
        # Executando pulo quando estiver acima do chão. Vai estar quando aperta o button == 0, pois o rect.y diminui em 1 unidade:
        if self.rect.bottom < self.pos_y:
            self.pular_movimentacao(self.direcao)

        # Atualizando a mask da Alice:
        self.mask = pygame.mask.from_surface(self.image)