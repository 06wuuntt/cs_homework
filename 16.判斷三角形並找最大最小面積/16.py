import math
def getTriangle(l:list):
    a,b,c = l[0],l[1],l[2]
    if (a+b<=c or a<0):
        print('not a triangle')
    elif (a == b and b == c and a == c):
        print('equilateral triangle',end=' ')
        getArea(l)
    elif ((a==b and a**2 + b**2 > c**2) or (b==c and b**2 + c**2 > a**2) or (a==c and a**2 + c**2 > b**2)):
        print('isosceles triangle',end=' ')
        getArea(l)
    elif (a**2 + b**2 < c**2):
        print('obtuse triangle',end=' ')
        getArea(l)
    elif (a**2 + b**2 > c**2):
        print('acute triangle',end=' ')
        getArea(l)
    elif (a**2 + b**2 == c**2):
        print('right triangle',end=' ')
        getArea(l)

def getArea(l:list):
    s = sum(l)/2
    area = round(math.sqrt(s*(s-l[0])*(s-l[1])*(s-l[2])),2)
    print(f'{area:.2f}')
    areas.append(area)
    return areas

def compare(a):
    if a == []:
        print('All inputs are not triangles!')
    else:
        print(f'{max(a):.2f}')
        print(f'{min(a):.2f}')

areas = []
triangles = []
n = int(input())
for i in range(n):
    triangle = sorted(list(map(int, input().split(' '))))
    triangles.append(triangle)
for i in range(n):
    getTriangle(triangles[i])
compare(areas)