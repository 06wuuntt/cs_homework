def reupdown(l):
    for i in range(len(l)-1,-1,-1):
        newmatrix.append(l[i])

def releftright(l):
    for i in range(0,len(l)):
        col = list()
        for j in range(len(l)-1,-1,-1):
            col.append(l[i][j])
        newmatrix.append(col)

def turnleft(l):
    for i in range(len(l)-1,-1,-1):
        col = list()
        for j in range(0,len(l)):
            col.append(l[j][i])
        newmatrix.append(col)

def turnright(l):
    for i in range(0,len(l)):
        col = list()
        for j in range(len(l)-1,-1,-1):
            col.append(l[j][i])
        newmatrix.append(col)

def main():
    n,direction = [int(input()) for i in range(0,2)]
    matrix = list()
    for i in range(0, n):
        col = [n*i+j for j in range(1,n+1)]
        matrix.append(col)
    if direction == 1:
        turnleft(matrix)
    elif direction == 2:
        turnright(matrix)
    elif direction == 3:
        reupdown(matrix)
    elif direction == 4:
        releftright(matrix)
    for i in newmatrix:
        for j in i:
            print(f'{j:3}',end = '')
        print('')

newmatrix = list()
main()