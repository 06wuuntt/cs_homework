def countLength(x1,x2):
    for i in range(x1,x2):
        line[20+i] = 1
        
line = [0]*40
a1,a2,b1,b2,c1,c2 = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
countLength(a1,a2)
countLength(b1,b2)
countLength(c1,c2)
print(line.count(1))