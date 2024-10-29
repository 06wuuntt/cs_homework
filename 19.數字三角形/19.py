def getRighttriangle(n):
    for i in range(1, n+1):
        drawNumber(1, i, 1)

def getTriangle(n):
    for i in range(1,n+1):
        drawMark('_', n-i)
        drawNumber(1, i, 0)
        drawMark('_', n-i)
        print('')

def getreTriangle(n):
    for i in range(n):
        for j in range(0,i):
            print('_', end = '')
        for j in range(1, n-i+1):
            print(j, end = '')
        for j in range(n-i-1, 0, -1):
            print(j, end = '')
        for j in range(0,i):
            print('_', end = '')
        print('')

def drawNumber(x, y, z):
    for i in range(x, y+1):
        print(i, end = '')
    for i in range(y-1, 0, -1):
        print(i, end = '')
    if z == 1:
        print('')

def drawMark(m,n):
    for i in range(n):
        print(m, end = '')

def main():
    m, n = int(input()), int(input())
    if m == 1:
        getRighttriangle(n)
    elif m == 2:
        getTriangle(n)
    elif m == 3:
        getreTriangle(n)

main()