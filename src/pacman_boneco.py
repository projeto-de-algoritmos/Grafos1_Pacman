import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1

class Pacman:
    #Construtor de classe A função __init__() é usada para inicializar os atributos do objeto da classe.
    # O parâmetro self é uma referência ao objeto que está sendo criado e é usado para acessar seus atributos e métodos.
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.tamanho = tamanho #Tamanho da tela pela quantidade de colunas
        self.raio = int(self.tamanho/2)
        self.colidiu = False
        self.corpo = pygame.Rect(self.centro_x, self.centro_y, self.centro_x, self.centro_y)
    
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
            #Movimentação do Pacman
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT: 
                    if self.colidiu == True:
                        self.velocidade_x = 0
                    else:
                        self.velocidade_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    if self.colidiu == True:
                        self.velocidade_x = -0 
                    else:    
                        self.velocidade_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    if self.colidiu == True:
                        self.velocidade_y = -0 
                    else:    
                        self.velocidade_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    if self.colidiu == True:
                        self.velocidade_y = 0 
                    else:    
                        self.velocidade_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT: self.velocidade_x = 0
                elif e.key == pygame.K_LEFT: self.velocidade_x = -0
                elif e.key == pygame.K_UP: self.velocidade_y = -0
                elif e.key == pygame.K_DOWN: self.velocidade_y = 0


