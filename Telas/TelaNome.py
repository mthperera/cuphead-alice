# 1. Módulos da biblioteca padrão
import json

# 2. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 3. Módulos locais
from constantes import *


def ler_jogadores_de_arquivo(caminho_arquivo : str) -> list[dict]:
    """
    Lê os jogadores do arquivo ranking.txt.

    Args:
        caminho_arquivo (str) : Caminho do arquivo txt.
    
    Returns:
        jogadores (list[dict]): Lista dos dicionários dos jogadores.
    """
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        jogadores = json.load(f)
    return jogadores


def mover_cursor(self, dx : int, dy : int) -> None:
    """
    Move o cursor dentro do teclado virtual.

    Args:
        dx (int): Deslocamento horizontal do cursor.
        dy (int): Deslocamento vertical do cursor.
    
    Returns:
        None:
    """

    self.cursor_y = max(0, min(self.cursor_y + dy, len(self.teclado) - 1))
    linha = self.teclado[self.cursor_y]
    self.cursor_x = max(0, min(self.cursor_x + dx, len(linha) - 1))


def processar_selecao(self) -> None:
    """
    Processa a tecla selecionada atualmente no teclado virtual.

    Ação depende da tecla:
        - "⌫": remove o último caractere.
        - "SPACE": adiciona espaço.
        - "OK": confirma o nome e muda de tela (se for válido).
        - Letra qualquer: adiciona ao nome.
    
    Returns:
        None:
    """
    letra = self.teclado[self.cursor_y][self.cursor_x]

    if letra == "⌫":
        self.nome = self.nome[:-1]
    elif letra == "SPACE":
        if len(self.nome) < self.max_caracteres:
            self.nome += " "
    elif letra == "OK":
        if len(self.nome) > 0:
            self.quantidade_mesmo_nome = 0 
            for jogador in self.lista_jogadores:
                if jogador["Nome"] == self.nome:
                    self.quantidade_mesmo_nome = 1
                    break
            if self.quantidade_mesmo_nome == 0:
                self.tela_atual = "TelaInicial"

    else:
        if len(self.nome) < self.max_caracteres:
            self.nome += letra


class TelaNome:
    """ 
    Representa a tela em que o jogador insere seu nome usando um teclado virtual.

    Essa tela permite que o jogador escolha seu nome navegando por um teclado renderizado,
    utilizando as setas do controle e botões para confirmar, apagar ou adicionar espaço.

    Attributes:
        tela_atual (str): Nome da tela atual (por padrão, "TelaNome").
        nome (str): Nome que está sendo digitado pelo jogador.
        max_caracteres (int): Número máximo de caracteres permitidos no nome.
        teclado (list[list[str]]): Teclas disponíveis organizadas por linhas.
        cursor_x (int): Posição horizontal atual do cursor no teclado.
        cursor_y (int): Posição vertical atual do cursor no teclado.
        fonte_nome (pygame.font.Font): Fonte utilizada para exibir o nome digitado.
        fonte_tecla (pygame.font.Font): Fonte utilizada nas teclas do teclado virtual.
        tempo_ultimo_mov (int): Tempo da última movimentação do cursor.
        delay_movimento (int): Delay em milissegundos entre os movimentos do cursor.
        lista_jogadores (list[dict]): Lista de jogadores já registrados (lida do arquivo).
        quantidade_mesmo_nome (int): Indicador de nomes repetidos. 0 se nome é único.
    """

    # Uma parte desse código foi gerada pelo ChatGPT 4o.
    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaInicial. 

        Returns:
            None:
        """
        self.tela_atual = "TelaNome"
        self.nome = ""
        self.max_caracteres = 15

        self.teclado = [
            list("QWERTYUIOP"),
            list("ASDFGHJKL"),
            list("ZXCVBNM"),
            ["⌫", "SPACE", "OK"]
        ]
        self.cursor_x = 0
        self.cursor_y = 0

        self.fonte_nome = pygame.font.SysFont("comicsansms", 48, bold=True)
        self.fonte_tecla = FONTE_TECLA

        self.tempo_ultimo_mov = 0
        self.delay_movimento = 200
        self.lista_jogadores = ler_jogadores_de_arquivo("ranking.txt")
        self.quantidade_mesmo_nome = 0

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo e as teclas.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill((25, 25, 25))
        window.blit(FUNDO_TELA_NOME, (0, 0))  


        # Desenhando Caixa do nome:
        caixa_nome = pygame.Rect(LARGURA_TELA // 2 - 400, 100, 800, 70)
        pygame.draw.rect(window, (50, 50, 50), caixa_nome, border_radius=10)
        pygame.draw.rect(window, (180, 180, 180), caixa_nome, 2, border_radius=10)

        texto_nome = self.fonte_nome.render(self.nome, True, (255, 255, 255))
        texto_nome_rect = texto_nome.get_rect(center=caixa_nome.center)
        window.blit(texto_nome, texto_nome_rect)


        # Desenhando teclado:
        base_y = 300 
        espaco_y = 75
        margem_vertical = 15

        for y, linha in enumerate(self.teclado):
            total_largura = sum([180 if l in ("SPACE", "OK") else 90 for l in linha]) + (len(linha) - 1) * 10
            base_x = (LARGURA_TELA - total_largura) // 2
            pos_x = base_x

            for x, letra in enumerate(linha):
                largura = 180 if letra in ("SPACE", "OK") else 90
                altura = 60

                rect = pygame.Rect(pos_x, base_y + y * (espaco_y + margem_vertical), largura, altura)

                cor = (120, 120, 120) if (x == self.cursor_x and y == self.cursor_y) else (220, 220, 220)
                pygame.draw.rect(window, cor, rect, border_radius=12)
                pygame.draw.rect(window, (60, 60, 60), rect, 2, border_radius=12)

                # Mostra o texto da tecla de forma segura
                texto_mostrar = letra  # Evita símbolos bugados
                fonte_usar = self.fonte_tecla.render(texto_mostrar, True, (0, 0, 0))
                text_rect = fonte_usar.get_rect(center=rect.center)
                window.blit(fonte_usar, text_rect)

                pos_x += largura + 10

        pygame.display.flip()

    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como eventos e teclas pressionadas.

        Returns:
            bool: 
                - True se continuar na tela.
        """
        now = pygame.time.get_ticks()

        # Verifica eventos e mudança de tela e de interações com as teclas:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"
                    
            elif evento.type == pygame.JOYAXISMOTION:
                if now - self.tempo_ultimo_mov > self.delay_movimento:
                    if evento.axis == 0:
                        if evento.value < -0.7:
                            self.mover_cursor(-1, 0)
                            self.tempo_ultimo_mov = now
                        elif evento.value > 0.7:
                            self.mover_cursor(1, 0)
                            self.tempo_ultimo_mov = now
                    elif evento.axis == 1:
                        if evento.value < -0.7:
                            self.mover_cursor(0, -1)
                            self.tempo_ultimo_mov = now
                        elif evento.value > 0.7:
                            self.mover_cursor(0, 1)
                            self.tempo_ultimo_mov = now

            elif evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.processar_selecao()
                elif evento.button == 1:
                    self.nome = self.nome[:-1]

        return True


