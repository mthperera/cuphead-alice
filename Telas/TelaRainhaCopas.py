from Classes.Cartinha import Cartinha
from Classes.Coracao import Coracao
from Classes.RainhaCopas import RainhaCopas
from constantes import *
from random import randint

class TelaRainhaCopas():

    def __init__(self):
        self.lista_cartinhas = list()
        self.lista_coracoes = list()
        self.rainha_copas = RainhaCopas()
        self.tela_atual = "TelaRainhaCopas"
        self.t0 = pygame.time.get_ticks()
        self.delta_t_acel = 5000
        self.delta_t_pers = 5000
        self.delta_t_coracao = 5000
        self.delta_t_remove = 15000


    def inicializa(self):
        pygame.init()

        # info = pygame.display.Info()
        # largura, altura = info.current_w, info.current_h
        # window = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)

        window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
 
        return window


    def gera_cartinhas_acelerando(self):
        if (pygame.time.get_ticks() - self.t0) // self.delta_t_acel > 0 and (pygame.time.get_ticks()- self.t0) < 60000:
            for _ in range(3):
                cartinha = Cartinha()
                cartinha.pos_x = POS_X + randint(-150, 50)
                cartinha.pos_y = POS_Y + randint(-200, 50)
                cartinha.velocidade_x = randint(-120, -10)
                cartinha.velocidade_y = randint(-50, -30)
                cartinha.movimento = "acelerando"
                self.lista_cartinhas.append(cartinha)

            self.delta_t_acel += 5000
    
    
    def gera_cartinhas_perseguindo(self):
        if (pygame.time.get_ticks() - self.t0 - 20000) // self.delta_t_pers > 0 and 25000 < (pygame.time.get_ticks()- self.t0) < 40000:
            for _ in range(3):
                cartinha = Cartinha()
                cartinha.pos_x = POS_X + randint(-200, 50)
                cartinha.pos_y = POS_Y + randint(-200, 50)
                cartinha.movimento = "perseguindo"
                self.lista_cartinhas.append(cartinha)

            self.delta_t_pers += 5000


    def gera_coracoes(self):
        if (pygame.time.get_ticks() - self.t0 - 30000) // self.delta_t_coracao > 0:
            for _ in range(12):
                coracao = Coracao()
                coracao.pos_y = randint(-700, -400)
                coracao.pos_x = randint(50, LARGURA_TELA - 100)
                self.lista_coracoes.append(coracao)
                self.rainha_copas.ataque_coracao = "Atacando"
                self.rainha_copas.t0_ataque = pygame.time.get_ticks()

            self.delta_t_coracao += 4000


    def desenha(self, window):
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_RAINHA_COPAS, (0, 0))
        
        for cartinha in self.lista_cartinhas:
            cartinha.desenhar(window)
        
        for coracao in self.lista_coracoes:
            coracao.desenhar(window)
        
        self.rainha_copas.desenhar(window)

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

        self.gera_cartinhas_acelerando()
        # self.gera_cartinhas_perseguindo()
        self.gera_coracoes()

        for coracao in self.lista_coracoes:
            if coracao.vivo == "Vivo":
                coracao.movimentar()
            if coracao.pos_y > ALTURA_TELA - 48 and coracao.vivo == "Vivo":
                coracao.t0_morte = pygame.time.get_ticks()
                coracao.vivo = "Morrendo"
            if coracao.vivo == "Morrendo":
                coracao.animar_morte()
            if coracao.vivo == "Morto":
                self.lista_coracoes.remove(coracao)


        for cartinha in self.lista_cartinhas:
            if cartinha.movimento == "acelerando" and cartinha.vivo == "Vivo":
                cartinha.movimentar_acelerando(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                cartinha.animar()
                cartinha.rotacionar()
            elif cartinha.vivo == "Morrendo":
                cartinha.animar_morte()
            elif cartinha.vivo == "Morto":
                self.lista_cartinhas.remove(cartinha)
            # elif cartinha.movimento == "perseguindo":
            #     cartinha.movimentar_perseguindo(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            #     cartinha.animar()

        if (pygame.time.get_ticks() - self.t0) // self.delta_t_remove > 0 and (pygame.time.get_ticks() - self.t0) < 100000:

            if len(self.lista_cartinhas) > 8:
                self.lista_cartinhas[0].vivo = "Morrendo"
                self.lista_cartinhas[0].t0_morte = pygame.time.get_ticks()
                self.lista_cartinhas[1].vivo = "Morrendo"
                self.lista_cartinhas[1].t0_morte = pygame.time.get_ticks()

                self.delta_t_remove += 10000
        
        if self.rainha_copas.ataque_coracao == "Atacando":
            self.rainha_copas.invocar_coracoes()
        
        self.rainha_copas.movimentar()

        return True
    
    