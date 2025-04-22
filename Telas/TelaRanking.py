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


def ranquear_jogadores(jogadores : list[dict]) -> list[dict]:
    """
    Lê os jogadores do arquivo ranking.txt e ordena eles em ordem de ranking:
        * 1º critério: Jogador com maior nível é melhor colocado.
        * 2º critério: 
            - Se estiver no nível 3: O menor tempo de conclusão é melhor colocado.
            - Caso não: O maior dano nos chefões é melhor colocado.
    
    Args:
        jogadores (list[dict]) : Lista de todos os jogadores.
    
    Returns:
        jogadores(list[dict]) : Lista de todos os jogadores em ordem.
    """
    def criterio(j):
        if j["Nível"] == 3:
            return (-j["Nível"], j["Tempo"])
        else:
            return (-j["Nível"], -j["Dano"])

    return sorted(jogadores, key=criterio)


def adiciona_jogador_no_ranking(jogador : dict, arquivo : str="ranking.txt") -> None:
    """
    Adiciona um jogador (o que acabou de jogar) ao arquivo ranking.txt.

    Args:
        jogador (dict): Informações do jogador, como Nome, Nível, Dano e Tempo.
        arquivo (str): Caminho do arquivo txt.
    
    Returns:
        None:
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            ranking = json.load(f)
    except:
        ranking = []
    ranking.append(jogador)

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)


class TelaRanking:
    """ 
    Representa a tela que mostra ao jogador a opção de instruções e início de jogo.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        t0 (int): Tempo em que a Tela é iniciada.
        fundo (Surface): Imagem de fundo.
        canal_0 (Channel): Canal utilizado para a música de fundo.
        jogador (dict): Informações do jogador, como Nome, Nível, Dano e Tempo.
    """

    def __init__(self, nome : str, nivel : int, dano : int, tempo_inicou : int, tempo_terminou : int) -> None:
        """ 
        Inicializa uma instância da classe TelaRanking. 
        
        Args:
            nome (str): Nome do jogador.
            nivel (int): Nível do jogador.
            tempo_iniciou (int): O tempo em que o jogador iniciou o jogo.
            tempo_terminou (int): O tempo em que o jogador terminou o jogo.

        Returns:
            None:
        """
        self.tela_atual = "TelaRanking"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_RANKING
        self.canal_0 = pygame.mixer.Channel(0)
        self.jogador = {
            "Nome" : nome, 
            "Nível": nivel,
            "Dano": dano,
            "Tempo": tempo_terminou - tempo_inicou,
        }

    def inicializa(self) -> None:
        """ 
        Inicializa a TelaRanking.
        Adiciona o personagem ao ranking, além de ler e ordenar. 

        Returns:
            None:
        """
        adiciona_jogador_no_ranking(self.jogador)
        lista_jogadores = ler_jogadores_de_arquivo("ranking.txt")
        self.lista_ranking = ranquear_jogadores(lista_jogadores)

        for i in range(len(self.lista_ranking)):
            if self.lista_ranking[i]["Nome"] == self.jogador["Nome"]:
                self.jogador["Posição"] = i + 1

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo e as cartas das fases.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill(BRANCO)
        window.blit(self.fundo, (0, 0))

        # Desenhando o TOP 5:
        for i in range(5):
            self.texto_nome = FONTE_RANKING_26.render(f"{self.lista_ranking[i]['Nome']}", True, (43, 31, 13))
            window.blit(self.texto_nome, (315, 350 + 65*i))
            self.texto_nivel = FONTE_RANKING_28.render(f"{self.lista_ranking[i]['Nível']}", True, (43, 31, 13))
            window.blit(self.texto_nivel, (735, 350 + 65*i))
            self.texto_dano = FONTE_RANKING_28.render(f"{self.lista_ranking[i]['Dano']}", True, (43, 31, 13))
            window.blit(self.texto_dano, (965, 350 + 65*i))
        
        # Desenhando ranking do jogador:
        self.jogador_nome = FONTE_RANKING_26.render(f"{self.jogador['Nome']}", True, (43, 31, 13))
        rect_nome = self.jogador_nome.get_rect(center=(LARGURA_TELA // 2 + 10, ALTURA_TELA - 80))
        window.blit(self.jogador_nome, rect_nome)
        texto = f"{self.jogador['Posição']} Lugar!"
        self.jogador_posicao = FONTE_RANKING_26.render(texto, True, (43, 31, 13))
        rect_posicao = self.jogador_posicao.get_rect(center=(LARGURA_TELA // 2 + 10, ALTURA_TELA - 45))
        window.blit(self.jogador_posicao, rect_posicao)

        pygame.display.flip()

    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como música, cartas viradas e eventos.

        Returns:
            bool: 
                - True se continuar na tela.
        """

        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            self.canal_0.play(MUSICA_FUNDO_ALICE, loops=-1)
        
        # Verifica eventos de troca de tela ou saída do jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair" 
                
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    if self.tela_atual == "Sair":
                        self.canal_0.stop()

        return True
    
    