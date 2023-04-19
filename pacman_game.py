import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

class Pacman:
    #Construtor de classe A função __init__() é usada para inicializar os atributos do objeto da classe.
    # O parâmetro self é uma referência ao objeto que está sendo criado e é usado para acessar seus atributos e métodos.
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.tamanho = 800 // 30 #Tamanho da tela pela quantidade de colunas
        self.raio = int(self.tamanho/2)
    
    def calcular_regras(self):
        #Movimentação 
        self.coluna += self.velocidade_x
        self.linha += self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
     

    def pintar(self, tela):
        #Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        #Desenhar a boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)
        #desenhar o olho
        olho_x = int(self.centro_x + self.raio/3)
        olho_y = int(self.centro_y - self.raio * 0.75)
        olho_raio = int(self.raio/10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 1
            elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_RIGHT:
                        self.velocidade_x = 0
                        



#verificar se esta iniciando o programa main
if __name__ == "__main__":
    pacman = Pacman()
    # Loop do jogo
    while True: 
        #Calcular regras
        pacman.calcular_regras()

        #Pintar a tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        #Captura de eventos
        eventos =  pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)   
