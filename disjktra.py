grafo = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'b':16,'e': 7,'h':9,'f':5}, 'e': {'d': 9,'f':20}, 'f':{'e':13,'h':7,'g':3}, 'g':{'i':14}, 'h':{'i':10,'g':11},'i':{'j':19},'j':{'e':15,'f':12}}


def dijkstra(grafo, comeco, objetivo):
    menor_distancia = {}
    predecessor = {}
    Nosnaopercorridos = grafo
    infinity = 9999999
    caminho = []
    for node in Nosnaopercorridos:
        menor_distancia[node] = infinity
    menor_distancia[comeco] = 0

    while Nosnaopercorridos:
        minNode = None
        for node in Nosnaopercorridos:
            if minNode is None:
                minNode = node
            elif menor_distancia[node] < menor_distancia[minNode]:
                minNode = node

        for childNode, peso in grafo[minNode].items():
            if peso + menor_distancia[minNode] < menor_distancia[childNode]:
                menor_distancia[childNode] = peso + menor_distancia[minNode]
                predecessor[childNode] = minNode
        Nosnaopercorridos.pop(minNode)

    currentNode = objetivo
    while currentNode != comeco:
        try:
            caminho.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Caminho nao alcancavel')
            break
    caminho.insert(0, comeco)
    if menor_distancia[objetivo] != infinity:
        print('Menor distancia é ' + str(menor_distancia[objetivo]))
        print('E o caminho é ' + str(caminho))


dijkstra(grafo, 'a', 'j')