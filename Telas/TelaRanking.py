import pygame
from constantes import *
import json


def ler_jogadores_de_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        jogadores = json.load(f)
    return jogadores


def ranquear_jogadores(jogadores):
    def criterio(j):
        if j["Nível"] == 3:
            return (-j["Nível"], j["Tempo"])
        else:
            return (-j["Nível"], -j["Dano"])

    return sorted(jogadores, key=criterio)


class TelaRanking():

    def __init__(self):
        self.tela_atual = "TelaRanking"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_RANKING
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)
        self.jogador = {
            "Nome" : "AAAAAAAAAA",
            "Posição" : 8
        }


    def inicializa(self):

        lista_jogadores = ler_jogadores_de_arquivo("ranking.txt")
        self.lista_ranking = ranquear_jogadores(lista_jogadores)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(self.fundo, (0, 0))

        for i in range(5):
            self.texto_nome = FONTE_RANKING_26.render(f"{self.lista_ranking[i]['Nome']}", True, (43, 31, 13))
            window.blit(self.texto_nome, (315, 350 + 65*i))
            self.texto_nivel = FONTE_RANKING_28.render(f"{self.lista_ranking[i]['Nível']}", True, (43, 31, 13))
            window.blit(self.texto_nivel, (735, 350 + 65*i))
            self.texto_dano = FONTE_RANKING_28.render(f"{self.lista_ranking[i]['Dano']}", True, (43, 31, 13))
            window.blit(self.texto_dano, (965, 350 + 65*i))
        
        
        self.jogador_nome = FONTE_RANKING_26.render(f"{self.jogador['Nome']}", True, (43, 31, 13))
        rect_nome = self.jogador_nome.get_rect(center=(LARGURA_TELA // 2 + 10, ALTURA_TELA - 80))
        window.blit(self.jogador_nome, rect_nome)
        texto = f"{self.jogador['Posição']} Lugar!"
        self.jogador_posicao = FONTE_RANKING_26.render(texto, True, (43, 31, 13))
        rect_posicao = self.jogador_posicao.get_rect(center=(LARGURA_TELA // 2 + 10, ALTURA_TELA - 45))
        window.blit(self.jogador_posicao, rect_posicao)


        pygame.display.flip()


    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_ALICE, loops=-1)
            self.musica_tocando = True
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair" 
                
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:
                    if self.tela_atual == "TelaVitoria":
                        self.canal_0.stop()

        return True
    
    