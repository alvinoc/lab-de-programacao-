class Node:

    def __init__(self, value):
        '''Método Construtor que aponta para o próximo e guarda o valor do dado'''
        
        self.value = value 
        self.prox = None


    def getvalue(self):
        return self.value

    def getprox(self):
        return self.prox

    def setvalue(self,i):
        self.value = i

    def setprox(self,i):
        self.prox = i


class Fila:

    def __init__(self):
        '''Método Construtor que aponta para inicio e fim'''
        
        self.inicio = None
        self.fim = None

    def __str__(self): #Método string que mostra toda a lista
        
        if self.IsEmpty():
            return '[]'
        
        correntNo = self.inicio
        
        string = '[' + str(correntNo.getvalue())
        
        correntNo = correntNo.getprox()
        
        while correntNo is not None:
            
            string += ", " + str(correntNo.getvalue())
            correntNo = correntNo.getprox()
            
        string = string + ']'
        return string
        

    def InserirNoFim(self,value):
        '''Método de inserir o item na fila'''
        no = Node(value)
        
        if self.IsEmpty():#Caso estaja vazia
            
            self.inicio = self.fim = no
        else:
            
            self.fim.setprox(no)
            self.fim = no

    def RemoverNoInicio(self):
        '''Método de remover termo da fila'''
        no = self.inicio
        if self.IsEmpty():
            
            pass # lista está vazia
        elif self.inicio == self.fim:#Se tive apenas um item
            
            self.inicio = self.fim = None
        else:
            
            self.inicio = self.inicio.getprox()
            
        return no

    def IsEmpty(self):
        return self.inicio == None


def create_grafo(vertices):
    '''Função que monta o grafo em uma matriz de adjacência'''
    grafo = [[]for a in range(vertices)]#Cria cada referência para cada vértice
    
    for vertice in range(vertices-1):# Ligações de cada vertice
        
        Vertice_1,Vertice_2 = map(lambda i: int(i), input().split())
        
        grafo[Vertice_1-1].append(Vertice_2-1)
        
        grafo[Vertice_2-1].append(Vertice_1-1)

    return grafo

def busca_em_largura(vertices,inicio,fim,grafo):
    '''Função que contem o algoritmo de busca em largura'''
    vizitados = [0]*vertices #A Lista de vizitados
    
    Queue = Fila() #A fila
    
    vertice = inicio    #Marcador do vertice que está vizitando
    
    Queue.InserirNoFim((inicio,0))#começa a fila ocm o vertice de inicio
    
    while vertice != fim:
        
        Data = Queue.RemoverNoInicio()  # pega o nó
        valores = Data.getvalue()   # obter o valor da tupla
        
        vertice,paradas = valores[0],valores[1]
        
        for vertice_vizinho in grafo[vertice]:#Anda por cada vertice vizinho
            
            if not vizitados[vertice_vizinho]:# Caso não foi vizitado
                
                vizitados[vertice_vizinho] = 1 #Coloca como vizitado
                
                Queue.InserirNoFim((vertice_vizinho,paradas+1)) #Inseri o nó na fila com o valor de paradas adicionada mais uma.
                
    return paradas
            
        

        
Cidades,inicio,fim = map(lambda i: int(i), input().split())

grafo = create_grafo(Cidades)

Paradas = busca_em_largura(Cidades,inicio-1,fim-1,grafo)

print(Paradas)