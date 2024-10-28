import math

a = eval(input())
b = eval(input())
c = eval(input())
x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
print(f'{x1:.1f}\n{x2:.1f}')
