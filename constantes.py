import pygame
import os

BRANCO = (255, 255, 255)

LARGURA_TELA = 800
ALTURA_TELA = 600

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

IMAGEM_FUNDO_RAINHA_COPAS = pygame.transform.scale(pygame.image.load(os.path.join("Assets\Imagens","Fundo_Rainha_Copas.png")), (LARGURA_TELA, ALTURA_TELA))

POS_X = 700
POS_Y = 500