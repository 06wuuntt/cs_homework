def getTriangle(a,b,c):
    if (a+b<c or a<0):
        print('not a triangle')
    elif (a == b and b == c and a == c):
        print('equilateral triangle')
    elif ((a==b and a**2 + b**2 > c**2) or (b==c and b**2 + c**2 > a**2) or (a==c and a**2 + c**2 > b**2)):
        print('isosceles triangle')
    elif (a**2 + b**2 < c**2):
        print('obtuse triangle')
    elif (a**2 + b**2 > c**2):
        print('acute triangle')
    elif (a**2 + b**2 == c**2):
        print('right triangle')
    
triangle = []
for i in range(3):
    a = int(input())
    triangle.append(a)
triangle.sort()
getTriangle(triangle[0],triangle[1],triangle[2])