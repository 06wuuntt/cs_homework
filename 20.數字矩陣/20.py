def turn(direction, m, times):
    if direction == 1:   # turn left
        for k in range(times):
            oldmatrix = m
            m = list()
            for i in range(n-1, -1, -1):
                l = list()
                for j in range(n):
                    l.append(oldmatrix[j][i])
                m.append(l)

    elif direction == 2: # turn right
        for k in range(times):
            oldmatrix = m
            m = list()
            for i in range(n):
                l = list()
                for j in range(n-1, -1, -1):
                    l.append(oldmatrix[j][i])
                m.append(l)
    for i in m:
        print(' '.join(map(str, i)))

def calculateandprint(ans):
    l = ans.count('L')
    r = ans.count('R')
    if l > r:
         turn(1, matrix, l-r)

    elif r > l:
        turn(2, matrix, r-l)
    else:
        for i in matrix:
            print(' '.join(map(str, i)))

def main():
    num = 1
    col = list()
    for i in range(n):
        col = list()
        for j in range(n):
            col.append(num)
            num += 1
        matrix.append(col)

    calculateandprint(ans)

n = int(input())
ans = input()
matrix = list()
main()  