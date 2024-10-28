def drawMark(mark,n):
    for i in range(n):
        print(mark,end='')

def drawTriangle(n):
    for i in range(1,n+1):
        drawMark('#',n-i)
        drawMark('*',2*i-1)
        drawMark('#',n-i)
        print('')

def drawRhombus(n):
    for i in range(n):
        drawMark()

def drawInvertedTriangle(n):
    for i in range(n,0,-1):
        drawMark('#',n-i)
        drawMark('*',2*i-1)
        drawMark('#',n-i)
        print('')



def main():
    c,n = int(input()),int(input())
    if n <= 2 or n >= 50 or n%2 == 0:
        print('error')
    else:
        if c == 1:
            drawTriangle(n)
        elif c == 2:
            drawInvertedTriangle(n)
        elif c == 3:
            drawRhombus(n)

main()