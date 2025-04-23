import pygame
import os

# Cores que serão usadas:
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
MARROM = (92, 64, 51)
CINZA = (83, 113, 110)


# Caracteres que serão usados:
CORACAO = chr(9829)


# Largura e altura da tela que serão usadas para criar a window:
pygame.init()
info = pygame.display.Info()
LARGURA_TELA, ALTURA_TELA = info.current_w, info.current_h


# Carregando a fonte para o teclado digital:
pygame.font.init()
FONTE_TECLA = pygame.font.Font(os.path.join("Assets/Fontes", "DejaVuSans.ttf"), 36)
FONTE_RANKING_22 = pygame.font.Font(os.path.join("Assets/Fontes", "ChailceNoggin.ttf"), 22)
FONTE_RANKING_26 = pygame.font.Font(os.path.join("Assets/Fontes", "ChailceNoggin.ttf"), 26)
FONTE_RANKING_28 = pygame.font.Font(os.path.join("Assets/Fontes", "ChailceNoggin.ttf"), 28)
FONTE_CORACAO = pygame.font.Font(os.path.join("Assets/Fontes", "PressStart2P.ttf"), 20)


# Carregando as músicas de fundo e os efeitos sonoros:
pygame.mixer.init()

MUSICA_FUNDO_ALICE = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Alice’s Theme.mp3"))
MUSICA_FUNDO_COELHO = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Corações e Desafios - Coelho.mp3"))
MUSICA_FUNDO_CARTAS = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Reflections of Defeat - Cartas.mp3"))
MUSICA_FUNDO_RAINHA_COPAS = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "A Rainha da Estratégia - RainhaCopas.mp3"))
MUSICA_FUNDO_TWEEDLE = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Whimsical Wonderland - Tweedle.mp3"))
MUSICA_FUNDO_RAINHA_VERMELHA = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Confronto da Rainha - RainhaVermelha.mp3"))
MUSICA_FUNDO_GAMEOVER = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "Prelude to Conflict - GameOver.mp3"))
MUSICA_FUNDO_VITORIA = pygame.mixer.Sound(os.path.join("Assets/Sons/Música Fundo", "achievements-and-motivation-303273.mp3"))

SOM_ALICE_ACERTOU = pygame.mixer.Sound(os.path.join("Assets/Sons/Sons Alice", "Acertou.mp3"))
SOM_ALICE_ATACANDO = pygame.mixer.Sound(os.path.join("Assets/Sons/Sons Alice", "Atacando.mp3"))
SOM_ALICE_DANO = pygame.mixer.Sound(os.path.join("Assets/Sons/Sons Alice", "Dano.mp3"))
SOM_ALICE_PULO = pygame.mixer.Sound(os.path.join("Assets/Sons/Sons Alice", "Pulo.mp3"))



# CARREGANDO AS IMAGENS:

# Alice:
LISTA_ALICE_BOLINHO = list()
LISTA_ALICE_CORRENDO = list()
LISTA_ALICE_PULANDO = list()
LISTA_ALICE_SUPER_BOLO = list()
LISTA_ALICE_AVIAO = list()
for i in range(1, 12):
    LISTA_ALICE_BOLINHO.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho/Alice Bolinho",f"{i}.png")), (170, 255)))
for i in range(1, 20):
    LISTA_ALICE_CORRENDO.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho/Alice Correndo",f"{i}.png")), (170, 255)))
for i in range(1, 9):
    LISTA_ALICE_PULANDO.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho/Alice Pulando",f"{i}.png")), (170, 255)))
for i in range(1, 12):
    LISTA_ALICE_SUPER_BOLO.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho/Alice SuperBolo",f"{i}.png")), (170, 255)))
for i in range(1, 14):
    LISTA_ALICE_AVIAO.append(pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho/Alice Avião",f"{i}.png")), (128, 128)))


# Quadro de vidas:
QUADRO_VIDAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho","Quadro Vidas.png")), (150, 100))


# Bolinho:
BOLINHO = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Alice e Bolinho","Bolinho.png")), (48, 48))


# Tela Nome:
FUNDO_TELA_NOME = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Nome","Fundo_Tela_Nome_01.png")), (LARGURA_TELA, ALTURA_TELA))


# Tela Inicial:
FUNDO_TELA_INICAL = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Inicial","Tela_Inicial_01.png")), (LARGURA_TELA, ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Inicial","Tela_Inicial_02.png")), (LARGURA_TELA, ALTURA_TELA)),
]


# Tela Instrucoes:
FUNDO_TELA_INSTRUCOES = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Instrucoes","Tela Instrucoes.png")), (LARGURA_TELA, ALTURA_TELA))


# Tela Coelho:
LISTA_FUNDO_COELHO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Coelho","Fundo_Coelho_01.png")), (LARGURA_TELA, ALTURA_TELA)),
]
LISTA_COELHO_CORRENDO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Coelho","Coelho_Correndo_02.png")), (170, 170)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Coelho","Coelho_Correndo_03.png")), (170, 170)),
]
LISTA_COELHO_PULANDO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Coelho","Coelho_Pulando_01.png")), (170, 170)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Coelho","Coelho_Pulando_02.png")), (170, 170)),
]


# Tela Cartas:
FUNDO_CARTAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Fundo_Tela_Cartas.png")), (LARGURA_TELA, ALTURA_TELA))
LISTA_CARTA_VIRADA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada_02.png")), (0.355*LARGURA_TELA, 0.87*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada_02.png")), (0.32*LARGURA_TELA, 0.87*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada_02.png")), (0.35*LARGURA_TELA, 0.87*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada.png")), (0.39*LARGURA_TELA, 0.97*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada.png")), (0.355*LARGURA_TELA, 0.97*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Cartas","Carta_Virada.png")), (0.38*LARGURA_TELA, 0.97*ALTURA_TELA)),
]


# Tela Rainha de Copas:
IMAGEM_FUNDO_RAINHA_COPAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Fundo_Rainha_Copas_4.png")), (LARGURA_TELA, ALTURA_TELA))
RAINHA_COPAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Rainha_Copas.png")), (255, 384))
LISTA_EXPLOSAO_CARTINHA  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_01.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_02.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_03.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_04.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_05.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Cartinha_06.png")), (32, 48)),
]
LISTA_INVOCAR_CORACAO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Invocar_Coracao_03.png")), (255, 384)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Invocar_Coracao_04.png")), (255, 384)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Invocar_Coracao_05.png")), (255, 384)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Invocar_Coracao_06.png")), (255, 384)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Invocar_Coracao_07.png")), (255, 384)),
]

LISTA_IMAGENS_CARTINHA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas", "Cartinha_Cima.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas", "Cartinha_Baixo.png")), (48, 48)),
]
LISTA_CORACAO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Coracao_01.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Coracao_02.png")), (48, 48)),
]
LISTA_EXPLOSAO_CORACAO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_01.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_02.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_03.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_04.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_05.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaCopas","Explosao_Coracao_06.png")), (32, 48)),
]


# Tela Tweedle Deen e Dum:
IMAGEM_FUNDO_TWEEDLE = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Fundo_Céu_01.png")), (LARGURA_TELA, ALTURA_TELA + 40))
IMAGEM_CASCA_OVO = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Casca_Ovo_03.png")), (196, 196))
LISTA_TEEDLE_OVO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Tweedle_Olho_Aberto.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Tweedle_Piscando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Tweedle_Preparando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Tweedle_Jogando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Tweedle_Recolhendo.png")), (128, 128)),
]
LISTA_OVOS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ovo_01.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ovo_02.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ovo_03.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ovo_04.png")), (32, 32)),
]
LISTA_IOIO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ioio_01.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Tweedle","Ioio_02.png")), (48, 48)),
]


# Tela Rainha Vermelha:
IMAGEM_FUNDO_RAINHA_VERMELHA = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Fundo_Rainha_Vermelha.png")), (LARGURA_TELA, ALTURA_TELA))
IMAGEM_PLATAFORMA_XADREZ = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Plataforma_Xadrez.png")), (7*ALTURA_TELA//8, 7*ALTURA_TELA//8))
IMAGEM_PLATAFORMA_RAINHA = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Plataforma_Rainha.png")), (256, 256))
IMAGEM_PLATAFORMA_REI = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Plataforma_Rainha.png")), (256, 256))
IMAGEM_RAINHA_BRANCA = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Rainha_Branca.png")), (128, 192))
LISTA_RAINHA_VERMELHA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Normal.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Piscando.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Estressada.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Atacando.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Ataca.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","RainhaVermelha_Voltando.png")), (170, 256)),
]
LISTA_REI = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","ReiVermelho_Abaixado.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","ReiVermelho_Levantado.png")), (170, 256)),
]
LISTA_LIVROS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Livro_01.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Livro_02.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Livro_03.png")), (48, 48)),
]
LISTA_PECAS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Bispo_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Torre_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela RainhaVermelha","Cavalo_Cinza.png")), (40, 60)),
]


# Tela GameOver:
FUNDO_GAME_OVER = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela GameOver","RainhaCopas.png")), (LARGURA_TELA, ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela GameOver","Tweedle.png")), (LARGURA_TELA, ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela GameOver","RainhaVermelha.png")), (LARGURA_TELA, ALTURA_TELA)),
]


# Tela Vitoria:
FUNDO_VITORIA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Vitoria","RainhaCopas.png")), (LARGURA_TELA, ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Vitoria","Tweedle.png")), (LARGURA_TELA, ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Vitoria","RainhaVermelha.png")), (LARGURA_TELA, ALTURA_TELA)),
]


# Tela Ranking:
FUNDO_TELA_RANKING = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Imagens/Tela Ranking","Fundo_Tela_Ranking.png")), (LARGURA_TELA, ALTURA_TELA))