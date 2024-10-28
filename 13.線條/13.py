def getLine(x11,x21):
    for i in range(x11,x21):
        line[20+i] = 1
line = [0]*40
n = int(input())
for i in range(n):
    x1,x2 = map(int,input().split(' '))
    getLine(x1,x2)
print(line.count(1))