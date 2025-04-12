import pygame
import os

BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
MARROM = (92, 64, 51)
CINZA = (83, 113, 110)

LARGURA_TELA = 800
ALTURA_TELA = 600

pygame.init()
info = pygame.display.Info()
LARGURA_TELA, ALTURA_TELA = info.current_w, info.current_h


LISTA_IMAGENS_CARTINHA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens", "Cartinha_Cima.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens", "Cartinha_Baixo.png")), (48, 48)),
]

MASKS_CARTINHA = [
    pygame.mask.from_surface(LISTA_IMAGENS_CARTINHA[0]),
    pygame.mask.from_surface(LISTA_IMAGENS_CARTINHA[1]),
]

IMAGEM_CORACAO = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Coracao.png")), (32, 48))

MASK_CORACAO = pygame.mask.from_surface(IMAGEM_CORACAO)

LISTA_EXPLOSAO_CORACAO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_01.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_02.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_03.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_04.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_05.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Coracao_06.png")), (32, 48)),
]

LISTA_EXPLOSAO_CARTINHA  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_01.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_02.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_03.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_04.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_05.png")), (32, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Explosao_Cartinha_06.png")), (32, 48)),
]

IMAGEM_FUNDO_RAINHA_COPAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Rainha_Copas_4.png")), (LARGURA_TELA, ALTURA_TELA))

IMAGEM_FUNDO_COELHO = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Coelho_01.png")), (LARGURA_TELA, ALTURA_TELA))

RAINHA_COPAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Rainha_Copas.png")), (170, 256))

LISTA_INVOCAR_CORACAO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_01.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_02.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_03.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_04.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_05.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_06.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Invocar_Coracao_07.png")), (170, 256)),
]

LISTA_COELHO_CORRENDO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Coelho_Correndo_02.png")), (170, 170)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Coelho_Correndo_03.png")), (170, 170)),
]

LISTA_COELHO_PULANDO  = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Coelho_Pulando_01.png")), (170, 170)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Coelho_Pulando_02.png")), (170, 170)),
]

PLATAFORMA_PEDRA = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Plataforma_Pedra.png")), (96, 96))

IMAGEM_FUNDO_DRAGAO = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Céu_01.png")), (LARGURA_TELA, ALTURA_TELA + 40))

LISTA_TEEDLE_OVO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Tweedle_Olho_Aberto.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Tweedle_Piscando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Tweedle_Preparando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Tweedle_Jogando.png")), (128, 128)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Tweedle_Recolhendo.png")), (128, 128)),
]

IMAGEM_CASCA_OVO = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Casca_Ovo_03.png")), (196, 196))

LISTA_IOIO = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ioio_01.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ioio_02.png")), (48, 48)),
]

LISTA_OVOS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ovo_01.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ovo_02.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ovo_03.png")), (32, 32)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Ovo_04.png")), (32, 32)),
]

IMAGEM_FUNDO_RAINHA_VERMELHA = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Rainha_Vermelha.png")), (LARGURA_TELA, ALTURA_TELA))

IMAGEM_PLATAFORMA_XADREZ = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Plataforma_Xadrez.png")), (7*ALTURA_TELA//8, 7*ALTURA_TELA//8))

IMAGEM_PLATAFORMA_RAINHA = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Plataforma_Rainha.png")), (256, 256))
IMAGEM_PLATAFORMA_REI = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Plataforma_Rainha.png")), (256, 256))

IMAGEM_RAINHA_BRANCA = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Rainha_Branca.png")), (128, 192))

LISTA_RAINHA_VERMELHA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Normal.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Piscando.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Estressada.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Atacando.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Ataca.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","RainhaVermelha_Voltando.png")), (170, 256)),
]

LISTA_LIVROS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Livro_01.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Livro_02.png")), (48, 48)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Livro_03.png")), (48, 48)),
]

LISTA_REI = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","ReiVermelho_Abaixado.png")), (170, 256)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","ReiVermelho_Levantado.png")), (170, 256)),
]

LISTA_PECAS = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Bispo.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Torre.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Cavalo.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Peão_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Bispo_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Torre_Cinza.png")), (40, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Cavalo_Cinza.png")), (40, 60)),
]

FUNDO_CARTAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Tela_Cartas.png")), (LARGURA_TELA, ALTURA_TELA))

LISTA_CARTA_VIRADA = [
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Carta_Virada.png")), (0.39*LARGURA_TELA, 0.97*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Carta_Virada.png")), (0.355*LARGURA_TELA, 0.97*ALTURA_TELA)),
    pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Carta_Virada.png")), (0.38*LARGURA_TELA, 0.97*ALTURA_TELA)),
]