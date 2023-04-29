   #Colisão de borda(works)
        if self.centro_x + self.raio > 800: self.velocidade_x = -1
        if self.centro_x - self.raio < 0: self.velocidade_x = 1
        if self.centro_y + self.raio > 600: self.velocidade_y = -1
        if self.centro_y - self.raio < 0: self.velocidade_y = 1


# Essa def é dentro de mapa, roda mas o visited so printa = {0}
 def bfs(self, start):
        visited = set()  # conjunto para armazenar os vértices visitados
        queue = deque([start])  # fila para armazenar os vértices a serem visitados
        n = len(self.matriz)  # número de vértices do grafo

        while queue:  # enquanto a fila não estiver vazia
            vertex = queue.popleft()  # retira o primeiro elemento da fila
            if vertex not in visited:  # verifica se o vértice já foi visitado
                visited.add(vertex)  # adiciona o vértice no conjunto de visitados
                for i in range(n):  # percorre os vértices adjacentes
                     if self.matriz[vertex][i] == 1 and i not in visited:  # verifica se existe uma aresta e se o vértice ainda não foi visitado
                         queue.append(i) 
        print(visited)



#Outro teste (not finished)
def shortestPath(self, start, end):
       sx = start[0]
       sy = start[1]
       dx = end[0]
       dy = end[1]
       #If starts or end value is 0, return
       print(self.matriz)
