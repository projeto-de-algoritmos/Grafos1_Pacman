import pygame
import pacman_boneco
import mapa
from pacman_boneco import Pacman
from mapa import Cenario

pygame.init()
screen = pygame.display.set_mode((600, 600), 0)

PRETO = (0, 0, 0)

#verificar se esta iniciando o programa main
if __name__ == "__main__":
    size = 600 // 30
    pacman = Pacman(size)
    cenario = Cenario(size)
    # Loop do jogo
    while True: 
        #Calcular regras
        pacman.calcular_regras()

        #Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        #Captura de eventos
        eventos =  pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)   
 