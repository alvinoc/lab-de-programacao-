class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * (vertices) for i in range(vertices)]


    def minDistance(self, dist, sptSet):
        min = float('inf')


        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def dijkstra(self, src):

        self.dist = dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):


            u = self.minDistance(dist, sptSet)


            sptSet[u] = True


            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]



def maximo(lista):

    maxv = lista[0]
    for i in lista:
        if i > maxv:
            maxv = i
    return maxv


def min(lista):
    minv = lista[0]
    for i in lista:
        if i<minv:
            minv = i
    return minv


lista_primeira_linha = list(map(int,input().split()))
vertices = lista_primeira_linha[0]#N
arestas = lista_primeira_linha[1]#M
g = Graph(vertices)
g.graph = [[0] * (vertices) for i in range(vertices)]

for i in range(arestas):
    inicio, fim, peso = [int(n) for n in input().split()]
    g.graph[inicio][fim] = peso
    g.graph[fim][inicio] = peso

distancias = []


for i in range(0,vertices):
    g.dijkstra(i)
    distancias.append(g.dist)

dist_max = []
for sublista in distancias:
    dist_max.append(maximo(sublista))

min(dist_max)
#print(distancias)
#print(dist_max)
print(min(dist_max))
#print(sublista)
#distancias.sort
#print(distancias)

'''for sublista in distancias:
    for elemento in '''
