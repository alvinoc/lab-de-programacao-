n = int(input())
soma = int()
lista = [int(n) for n in input().split()]
movimentos = int()
for i in range(n):
    soma = soma + lista[i]

soma = soma - n*(n+1)/2

if soma %n ==0:
    movimentos = 0
    altura = soma/n +1
    for i in range(n):
        if lista[i]>altura:
            movimentos = movimentos + lista[i]-altura
            altura = altura +1
    print(movimentos)
else: print("-1")
