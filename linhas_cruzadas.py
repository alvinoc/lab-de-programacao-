def mergeSort(array):
    inv = 0
    if len(array) > 1:
        mid = len(array) // 2  
        L = array[:mid] 
        R = array[mid:] 
    
        inv += mergeSort(L) 
        inv += mergeSort(R)

        L.append(float("inf"))
        R.append(float("inf"))

        j, k = 0, 0   
        for i in range(len(array)):
            if L[j] <= R[k]:
                array[i] = L[j]
                j += 1
            else:
                array[i] = R[k]
                k += 1
                inv += len(L) - j - 1

    return inv
 
def main():
        n = int(input())
        array = [int(i) for i in input().split()]
        print(mergeSort(array))

main()