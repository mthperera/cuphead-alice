import pygame
from constantes import *
from Classes.PlataformaXadrez import PlataformaXadrez
from Classes.PlataformaRainha import PlataformaRainha
from Classes.PlataformaRei import PlataformaRei
from Classes.RainhaVermelha import RainhaVermelha
from Classes.ReiVermelho import ReiVermelho
from Classes.Alice.AliceRainhaVermelha import AliceRainhaVermelha

class TelaRainhaVermelha():

    def __init__(self):
        self.tela_atual = "TelaRainhaVermelha"
        self.nivel = 2
        self.dano = 0
        self.tempo_terminou = 0
        self.t0 = pygame.time.get_ticks()
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceRainhaVermelha(LARGURA_TELA//2, ALTURA_TELA//2 - 110)
        self.alice.tela_atual = "TelaRainhaVermelha"
        self.grupo_alice.add(self.alice)
        self.grupo_plataforma = pygame.sprite.Group()
        self.grupo_plataforma.add(PlataformaXadrez())
        self.grupo_plataforma_rainha = pygame.sprite.Group()
        self.plataforma_rainha = PlataformaRainha()
        self.grupo_plataforma_rainha.add(self.plataforma_rainha)
        self.grupo_plataforma_rei = pygame.sprite.Group()
        self.plataforma_rei = PlataformaRei()
        self.grupo_plataforma_rei.add(self.plataforma_rei)
        self.grupo_rainha = pygame.sprite.Group()
        self.rainha_vermelha = RainhaVermelha(LARGURA_TELA - 210, 68, self.alice)
        self.grupo_rainha.add(self.rainha_vermelha)
        self.grupo_rei = pygame.sprite.Group()
        self.rei_vermelho = ReiVermelho(50, 70)
        self.grupo_rei.add(self.rei_vermelho)
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(IMAGEM_FUNDO_RAINHA_VERMELHA, (0, 0))
        window.blit(IMAGEM_RAINHA_BRANCA, (LARGURA_TELA//2 - IMAGEM_RAINHA_BRANCA.get_width()//2, 0))

        self.grupo_plataforma.draw(window)
        self.grupo_plataforma_rainha.draw(window)
        self.grupo_plataforma_rei.draw(window)
        self.grupo_rainha.draw(window)
        self.grupo_rei.draw(window)
        for rainha in self.grupo_rainha:
            rainha.grupo_livros.draw(window)
        for rei in self.grupo_rei:
            rei.grupo_pecas.draw(window)
        self.grupo_alice.draw(window)
        self.alice.grupo_bolinhos.draw(window)
        

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_RAINHA_VERMELHA, loops=-1)
            self.musica_tocando = True
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
                self.canal_0.stop()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"
                    self.canal_0.stop()
        

        if len(self.grupo_rainha) > 0:
            if pygame.sprite.spritecollide(self.alice, self.rainha_vermelha.grupo_livros, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
            if pygame.sprite.spritecollide(self.rainha_vermelha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rainha_vermelha.vidas -= 1
            if pygame.sprite.spritecollide(self.plataforma_rainha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rainha_vermelha.vidas -= 1
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha_vermelha.grupo_livros, True, True, pygame.sprite.collide_mask):
                pass

        if len(self.grupo_rei) > 0:
            if pygame.sprite.spritecollide(self.alice, self.rei_vermelho.grupo_pecas, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
            if pygame.sprite.spritecollide(self.rei_vermelho, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rei_vermelho.vidas -= 1
            if pygame.sprite.spritecollide(self.plataforma_rei, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rei_vermelho.vidas -= 1
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rei_vermelho.grupo_pecas, True, True, pygame.sprite.collide_mask):
                pass
        
        self.grupo_plataforma.update()
        self.grupo_plataforma_rainha.update()
        self.grupo_plataforma_rei.update()
        self.grupo_rainha.update()
        self.grupo_rei.update()
        for rainha in self.grupo_rainha:
            rainha.grupo_livros.update()
        for rei in self.grupo_rei:
            rei.grupo_pecas.update()
        self.alice.update(lista_eventos)
        self.alice.grupo_bolinhos.update()

        if self.alice.rect.centerx > 3.5*ALTURA_TELA//8 + LARGURA_TELA//2 or self.alice.rect.centerx < - 3.5*ALTURA_TELA//8 + 65 + LARGURA_TELA//2:
            if not self.alice.caindo:
                self.alice.t0_caindo = pygame.time.get_ticks()
                self.alice.caindo = True
            self.alice.cair()
        else:
            self.alice.movimentar_plataforma()

        if self.alice.vidas <= 0:
            self.tela_atual = "TelaGameOver"
            self.nivel = 2
            self.dano = 20 - self.rainha_vermelha.vidas + 20 - self.rei_vermelho.vidas
        
        if len(self.grupo_rainha) + len(self.grupo_rei) == 0:
            self.tela_atual = "TelaRanking"
            self.tempo_terminou = pygame.time.get_ticks()//1000
            self.nivel = 3
            self.dano = 40

        return True
    
    