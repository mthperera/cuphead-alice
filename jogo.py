import pygame
from Telas.Jogo import Jogo

if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() == 1:
        controle = pygame.joystick.Joystick(0)
        controle.init()
        jogo=Jogo()
        jogo.inicializa()

pygame.quit()