from Classes.Alice.AliceRainhaCopas import AliceRainhaCopas
from Classes.RainhaCopas import RainhaCopas
from constantes import *

def verifica_colisao(entidade_1: pygame.sprite.Sprite, entidade_2: pygame.sprite.Sprite):
    
    delta_x = entidade_2.rect.x - entidade_1.rect.x
    delta_y = entidade_2.rect.y - entidade_1.rect.y

    if entidade_2.mask.overlap(entidade_1.mask, (delta_x, delta_y)) is None:
        return False
    
    return True

class TelaRainhaCopas():

    def __init__(self):
        self.tela_atual = "TelaRainhaCopas"
        self.nivel = 0
        self.dano = 0
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceRainhaCopas(400, ALTURA_TELA - 50)
        self.grupo_alice.add(self.alice)
        self.grupo_rainha = pygame.sprite.Group()
        self.rainha = RainhaCopas(self.alice)
        self.grupo_rainha.add(self.rainha)
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_RAINHA_COPAS, (0, 0))
        
        for rainha in self.grupo_rainha:
            rainha.grupo_cartinhas.draw(window)
            rainha.grupo_coracoes.draw(window)
        
        self.grupo_alice.draw(window)
        for alice in self.grupo_alice:
            alice.grupo_bolinhos.draw(window)

        self.grupo_rainha.draw(window)

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_RAINHA_COPAS, loops=-1)
            self.musica_tocando = True

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"


        self.grupo_rainha.update()
        self.grupo_alice.update(lista_eventos)
        for alice in self.grupo_alice:
            alice.grupo_bolinhos.update()
        

        if verifica_colisao(self.rainha, self.alice):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000 and not self.alice.pulando:
                self.alice.vidas -= 1
                self.alice.t0_pular_rainha = pygame.time.get_ticks()
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                self.alice.colidindo_rainha = True

        if pygame.sprite.spritecollide(self.alice, self.rainha.grupo_cartinhas, True, pygame.sprite.collide_mask):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                self.alice.vidas -= 1
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
        if pygame.sprite.spritecollide(self.alice, self.rainha.grupo_coracoes, True, pygame.sprite.collide_mask):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                self.alice.vidas -= 1
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
        if pygame.sprite.spritecollide(self.rainha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
            self.rainha.vidas -= 2
        if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha.grupo_cartinhas, True, True, pygame.sprite.collide_mask):
            pass
        if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha.grupo_coracoes, True, True, pygame.sprite.collide_mask):
            pass
                
        if self.rainha.vidas <= 0:
            self.tela_atual = "TelaCartas"
            self.nivel = 1
            self.dano = 30

        if self.alice.vidas <= 0:
            self.tela_atual = "TelaGameOver"
            self.nivel = 0
            self.dano = 30 - self.rainha.vidas

        if len(self.grupo_alice) > 0:    
            for rainha in self.grupo_rainha:
                for alice in self.grupo_alice:
                    for cartinha in rainha.grupo_cartinhas:
                            if cartinha.vivo == "Vivo":
                                cartinha.movimentar_acelerando()
                                cartinha.rotacionar()
                    rainha.grupo_cartinhas.update()
                    rainha.grupo_coracoes.update()

        return True
    
    