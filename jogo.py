import pygame
from Telas.Jogo import Jogo

if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    controle = pygame.joystick.Joystick(0)
    controle.init()
    print(pygame.joystick.get_count())
    jogo=Jogo()
    jogo.inicializa()

pygame.quit()