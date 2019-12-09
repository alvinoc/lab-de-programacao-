def DFS(graph, current, pai, destiny, distance): 
    if current == destiny:
        print(distance)
        return True
    for v in graph[current-1]:
        if v != pai: 
            if DFS(graph, v, current, destiny, distance+1):
                return True
    return False

def main():
    vertex, source, destiny = [int(n) for n in input().split()]
    graph = [[] for i in range(vertex)]
    visiteds = [False] * (len(graph))
    for i in range(vertex-1):
        v1, v2 = [int(n) for n in input().split()]
        graph[v1-1] += [v2]
        graph[v2-1] += [v1]
    DFS(graph, source, source, destiny, 0)
main()