a = [str(x) for x in input("Digite os movimentos do robo: t ou f")]

t = int(a.count('t'))
f = int(a.count('f'))
inicio = 0
resultado = 0 + f - t
if t<f:
    resultado = resultado *(-1)
    print("resultado negativo, pois o robo andou para tras ")
if resultado ==0:
    print("posicao final igual a posicao inicial")
else: print("posicao final nao é igual a posicao inicial")
print(resultado)
print(a)


