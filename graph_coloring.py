lista_de_estados = []
fronteiras_abertas = True
lista_de_fronteiras = {}
while fronteiras_abertas:
    # loop para inserir o grafo
    estado = input("digite o estado ")
    fronteiras= input("quais as fronteiras desse estado?").split()
    lista_de_estados.append(estado)
    lista_de_fronteiras[estado] = fronteiras
    condicao = input("quer adicionar mais estados e fronteiras ? ('sim' para continuar, 'nao' para sair )")
    if condicao == 'nao':
        fronteiras_abertas = False


cores = ['Vermelho', 'Azul', 'Verde','Roxo','Laranja']

cores_dos_estados = {}

def colorir(estado, cor):
    for vizinho in lista_de_fronteiras.get(estado):
        cor_dos_vizinhos = cores_dos_estados.get(vizinho)
        if cor_dos_vizinhos == cor:
            return False

    return True

def get_cor_para_estados(estado):
    for cor in cores:
        if colorir(estado, cor):
            return cor


for estado in lista_de_estados:
    cores_dos_estados[estado] = get_cor_para_estados(estado)

print(cores_dos_estados)


