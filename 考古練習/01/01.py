def drawmark(n,m):
    for i in range(0,n):
        print(m,end = '')

def graph1(n):
    for i in range(1,n+1):
        print((str(i)*i).ljust(5,'#'))

def graph2(n):
    drawmark(2*(col-n),'#')
    for i in range(1,n+1):
        print(i, end = '')
    for i in range(n-1,0,-1):
        print(i, end = '')

def graph3(n, k):
    if k == 0:
        for i in range(1,n+1):
            print(i, end = '')
    elif k == 1:
        for i in range(n,0,-1):
            print(i, end = '')
    drawmark(col-n,'^')

def graph4(n,k):
    drawmark(col-n,'^')
    if k == 0:
        for i in range(n,1,-1):
            print(i,end = '')
        for i in range(1,n+1):
            print(i,end = '')
    elif k == 1:
        for i in range(n,1,-1):
            print(i,end = '')
        for i in range(n, 0 , -1):
            print(i, end = '')
    drawmark(col-n,'^')
        

def main():
    if graphtype == 1:
        graph1(col)
    elif graphtype == 2:
        for i in range(1, col+1):
            graph2(i)
            print('')
    elif graphtype == 3:
        for i in range(1, col+1):
            graph3(i, 0)
            print('')
        for i in range(col, 0, -1):
            graph3(i, 1)
            print('')
    elif graphtype == 4:
        for i in range(1,col+1):
            graph4(i, 0)
            print('')
        for i in range(col-1, 0, -1):
            graph4(i,1)
            print('')

graphtype = int(input())
col = int(input())
main()