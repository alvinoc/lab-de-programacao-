def count(matrix, l, c, line, col):
        flag = 1
        matrix[l][c] = "X"
        
        if l - 1 >= line and matrix[l - 1][c] == '#':
            flag = 0
        elif l - 1 >= line and matrix[l - 1][c] == 'F':
            flag = count(matrix, l - 1, c, line, col) and flag

        if l + 1 < line and matrix[l + 1][c] == '#':
            flag = 0
        elif l + 1 < line and matrix[l+1][c] == 'F':
            flag = count(matrix, l+1, c, line, col) and flag

        if c - 1 >= col and matrix[l][c - 1] == '#':
            flag = 0
        elif c - 1 >= col and matrix[l][c - 1] == 'F':
            flag = count(matrix, l, c - 1, line, col) and flag

        if c + 1 < col and matrix[l][c + 1] == '#':
            flag = 0
        elif c + 1 < col and matrix[l][c + 1] == 'F':
            flag = count(matrix, l, c + 1, line, col) and flag
            
        return flag


def main():

        line, col = [int(x) for x in input().split()]
        
        matrix = [[0] * (line) for i in range(col)]
        
        for i in range(line):
            matrix.append(i)
            matrix[i] = list(input())
    
        shots_amount = int(input())
        
        for i in range(shots_amount):
            l, c = [int(x) for x in input().split()]
            if matrix[l-1][c-1] == "#":
                matrix[l-1][c-1] = "F"

        destroyed = 0
        for i in range(line):
            
            for j in range(col):
                if matrix[i][j] == "F" and count(matrix, i, j, line, col):
                    destroyed += 1
                j += 1
                
        print(destroyed)

main()