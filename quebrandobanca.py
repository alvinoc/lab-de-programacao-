def partition(s, low, high, increase):
    i = low - 1
    pivot = s[high]
    for j in range(low, high):
        if increase:
            if s[j] < pivot:
                i += 1
                s[i], s[j] = s[j], s[i]
        else:
            if s[j] > pivot:
                i += 1
                s[i], s[j] = s[j], s[i]

    s[i+1], s[high] = s[high], s[i+1]
    return i + 1

def q_sort(s, low, high, increase=0):
    if (low < high):
        pi = partition(s, low, high, increase)
        q_sort(s, low, pi-1, increase)
        q_sort(s, pi+1, high, increase)

while True:
    try:
        a, b = [int(x) for x in input().split()]
        s = [int(x) for x in input()]
        copy = s[::]
    except:
        break
    
    index = []
    q_sort(copy, 0, len(s)-1)
    for i in range(a - b):
        index += [s.index(copy[i])]
    
    q_sort(index, 0, len(index)-1, 1)

    for i in index:
        print(s[i], end='')
    print()