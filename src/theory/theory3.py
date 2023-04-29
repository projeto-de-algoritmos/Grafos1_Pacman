import sys
import queue
import pygame
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

class Cell  :
    def __init__(self, x, y, dist, prev) :
        self.x = x # Linha
        self.y = y # Coluna
        self.dist = dist; #distance to start
        self.prev = prev; #parent cell in the path
    def __str__(self): #Printar como uma string
        return "("+ str(self.x) + "," + str(self.y) + ")" 

    
class ShortestPathBetweenCellsBFS :
    def __init__(self, tamanho, matrix):
        self.tamanho = tamanho
        self.matriz = matrix

    #BFS, Time O(n^2), Space O(n^2)
    def shortestPath(self, tamanho, tela, matrix, start, end) :
        tam = tamanho
        sx = start[0]
        sy = start[1]
        dx = end[0]
        dy = end[1]
		#if start or end value is 0, return
        if matrix[sx][sy] == 0 or matrix[dx][dy] == 0 :
            print("There is no path.")
            return  
		#initialize the cells 
        m = len(matrix)
        n = len(matrix[0])    
        cells = []
        for i in range (0, m) :
            row = []
            for j in range(0, n) :               
                if matrix[i][j] != 0 :
                    row.append(Cell(i, j, sys.maxsize, None))
                else:
                    row.append(None)
            cells.append(row) 
	    #breadth first search
        queue = []     
        src = cells[sx][sy]
        src.dist = 0
        queue.append(src)
        dest = None
        p = queue.pop(0)
        while p != None :
	    	#find destination 
            if p.x == dx and p.y == dy : 
                dest = p
                break	             
	        # moving up
            self.visit(cells, queue, p.x-1, p.y, p)    
            # moving left
            self.visit(cells, queue, p.x, p.y-1, p)     
	        # moving down
            self.visit(cells, queue, p.x+1, p.y, p)             
	        #moving right
            self.visit(cells, queue, p.x, p.y+1, p)
            if len(queue) > 0:
                p = queue.pop(0)
            else:
                p = None       
	    #compose the path if path exists
        if dest == None :
            print("there is no path.")
            return
        else :
            path = []
            p = dest
            while p != None :
                path.insert(0, p)	      
                p = p.prev      
            return path    
	
	#function to update cell visiting status, Time O(1), Space O(1)
    def visit(self, cells, queue, x, y, parent) :		
        #out of boundary
        if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None :
	        return
	    #update distance, and previous node
        dist = parent.dist + 1
        p = cells[x][y]
        if dist < p.dist :
            p.dist = dist
            p.prev = parent
            queue.append(p)
    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha): # pegar os valores da coluna na linha
            x = numero_coluna * self.tamanho #self.tamanho pode ser o tamanho do no
            y = numero_linha * self.tamanho
            cor = PRETO
            if coluna == 0: cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0) #(x,y)= posição de onde vai ser o retangulo, self.tamanho = tamanho do retangulo
            
    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz): #numero_linha = conteudo da linha, linha = posição da linha, função enumerate devolve a posição e o valor 
            self.pintar_linha(tela, numero_linha, linha) 
                       
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

#Começando o pygame
pygame.init()
screen = pygame.display.set_mode((600, 600), 0)

#verificar se esta iniciando o programa main
if __name__ == "__main__":

    size = 600 // 30
    myObj = ShortestPathBetweenCellsBFS(size, matrix)   
    #Test 
    start1 = [1, 1]
    end1 = [27, 5]
    
    # AQUI QUE TA O CAMINHO DAS PEDRAS
    teste = []
    teste = myObj.shortestPath(size, screen, matrix, start1, end1)
    for i in teste:
           print(i)

    # Loop do jogo
    while True: 
        #Pintar a tela
        screen.fill(PRETO)
        myObj.pintar(screen)
        pygame.display.update()
        #myObj.shortestPath(size, screen, matrix, start1, end1)
        #pygame.display.update()
        pygame.time.delay(1000)

        #Captura de eventos
        eventos =  pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        #pacman.processar_eventos(eventos)   
 