import pygame
from constantes import *
import json

def ler_jogadores_de_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        jogadores = json.load(f)
    return jogadores


class TelaNome:

    # Uma parte desse código foi gerada pelo ChatGPT 4o.
    def __init__(self):
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


    def desenha(self, window):
        window.fill((25, 25, 25))

        window.blit(FUNDO_TELA_NOME, (0, 0))  

        # Caixa do nome
        caixa_nome = pygame.Rect(LARGURA_TELA // 2 - 400, 100, 800, 70)
        pygame.draw.rect(window, (50, 50, 50), caixa_nome, border_radius=10)
        pygame.draw.rect(window, (180, 180, 180), caixa_nome, 2, border_radius=10)

        texto_nome = self.fonte_nome.render(self.nome, True, (255, 255, 255))
        texto_nome_rect = texto_nome.get_rect(center=caixa_nome.center)
        window.blit(texto_nome, texto_nome_rect)

        # Teclado
        base_y = 300  # Mais abaixo
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


    def atualiza_estado(self):
        tempo_atual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"
                    
            elif evento.type == pygame.JOYAXISMOTION:
                if tempo_atual - self.tempo_ultimo_mov > self.delay_movimento:
                    if evento.axis == 0:
                        if evento.value < -0.7:
                            self.mover_cursor(-1, 0)
                            self.tempo_ultimo_mov = tempo_atual
                        elif evento.value > 0.7:
                            self.mover_cursor(1, 0)
                            self.tempo_ultimo_mov = tempo_atual
                    elif evento.axis == 1:
                        if evento.value < -0.7:
                            self.mover_cursor(0, -1)
                            self.tempo_ultimo_mov = tempo_atual
                        elif evento.value > 0.7:
                            self.mover_cursor(0, 1)
                            self.tempo_ultimo_mov = tempo_atual

            elif evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.processar_selecao()
                elif evento.button == 1:
                    self.nome = self.nome[:-1]

        return True


    def mover_cursor(self, dx, dy):
        self.cursor_y = max(0, min(self.cursor_y + dy, len(self.teclado) - 1))
        linha = self.teclado[self.cursor_y]
        self.cursor_x = max(0, min(self.cursor_x + dx, len(linha) - 1))


    def processar_selecao(self):
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
