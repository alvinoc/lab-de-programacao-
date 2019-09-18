def visit_position(list_results, list_visited):

    #retorna a posicai na lista de resultados do menor valor que ainda nao foi visitado

    global smallest_position
    list_smallest = []
    smallest_value = float('inf')

    for i in range(0, len(list_visited)):
        if list_results[i] != float('inf') and list_visited[i] == 0:
            list_smallest.append(i)

    for i in range(0, len(list_smallest)):

        if list_results[list_smallest[i]] < smallest_value:
            smallest_value = list_results[list_smallest[i]]
            smallest_position = list_smallest[i]

    return smallest_position



list_first_line = list(map(int, input(''
                                      'Nessa primeira linha vc irá digitar 4 numeros de acordo com o passo-a-passo a seguir:\n'
                                      'O primeiro numero de entrada é o número total de vértices (cidades)do grafo\n'
                                      'O segundo numero de entrada é o total de arestas conectadas no grafo\n'
                                      'o terceiro numero será o local de partida e o quarto aonde vc quer ir para determinar o menor caminho\n'
                                      'A partir dessa linha vc irá digitar somente os vertices que estao ligados entre si e os respectivos pesos\n'
                                      'Ex: de entrada na primeira linha: 8(numero total de vertices/cidades), 6(numero de ligacoes entre os vertices/cidades)\n,'
                                      '5(esse 5 é o "apelido" da cidade, e onde vai ser o local de partida),8(mesma lógica do 5, sendo o local de chegada)\n'
                                      'A partir da 2 linha em diante, ou N-1 ésima linha, sendo N o numero total de cidades/vertices, vc irá digitar o vértice e o\n'
                                      'proximo com o que ele esta ligado e o peso dessa ligacao(peso da aresta). Ex de entrada a partir da N-1 ésima linha:\n'
                                      '5 8 10 (cidade/vertice 5 esta ligada com a cidade/vertice 8 e essa aresta possui peso 10)\n ').split()))

crosses = list_first_line[0]
roads = list_first_line[1]
starting_point = list_first_line[2] - 1
ending_point = list_first_line[3] - 1

list_addresses = []

for i in range(0, roads):
    list_addresses.append(list(map(int, input().split())))

list_matrix = [[float('inf') for i in range(crosses)] for j in range(crosses)]
list_total_results = []
list_total_coming_from = [0] * crosses


for i in range(0, (roads)):
    from_street = list_addresses[i][0] - 1
    to_street = list_addresses[i][1] - 1
    value_street = list_addresses[i][2]

    list_matrix[from_street][to_street] = value_street
    list_matrix[to_street][from_street] = value_street

matrix_visited_peaks = []

list_results = []
list_visited = []

list_results = [float('inf')] * crosses
list_visited = [0] * crosses
list_results[starting_point] = 0


# o visitado foi atribuido a -1 pra ser diferente da variavel do vertice de chegada(ending point)
visiting_currently = -1
list_total_coming_from[starting_point] = -1

while visiting_currently != ending_point:
    visiting_currently = visit_position(list_results, list_visited)
    current_value = list_results[visiting_currently]
    list_visited[visiting_currently] = 1

    for i in range(0, crosses):
        if list_matrix[visiting_currently][i] != 0 and list_matrix[visiting_currently][i] + current_value < \
                list_results[i]:
            list_results[i] = list_matrix[visiting_currently][i] + current_value
            last_updated_value = i
            list_total_coming_from[last_updated_value] = visiting_currently + 1
print(list_results[ending_point])
list_total_results.extend(list_results)

start_from = ending_point

result_to_display = []
result_to_display.append(ending_point + 1)

# -2 por que termina em -1 e é removido 1 da resposta, logo -1 -1 = -2
while (start_from != -2):
    start_from = list_total_coming_from[start_from] - 1
    if start_from != -2:
        result_to_display.append(start_from + 1)

print(result_to_display[::-1])  # [::-1] serve para inverter a lista ja que o metodo append sempre adiciona no final, mostrando o caminho invertido