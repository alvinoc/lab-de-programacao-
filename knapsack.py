def knapSack(capacity , weight , val , n): 
  
    if n == 0 or capacity == 0 : 
        return 0
  
 
    if (weight[n-1] > capacity): 
        return knapSack(capacity , weight , val , n-1) 
  
    
    else: 
        return maximo(val[n-1] + knapSack(capacity-weight[n-1] , weight , val , n-1), 
                   knapSack(capacity , weight , val , n-1)) 

def maximo(num1,num2):
    if num1>num2:
        return num1
    else: return num2
  

def main():
    n,capacidade = [int(x) for x in input().split()]
    valor = [0]*n
    peso = [0]*capacidade
    for i in range(n):
        peso[i], valor[i] = [int(x) for x in input().split()]
    print(knapSack(capacidade,peso,valor,n))

main()
  