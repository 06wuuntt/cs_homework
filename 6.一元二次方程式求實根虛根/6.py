	
import math
def func(a,b,c):
 
    is_virtual = False
 
    result = b*b-4*a*c
 
    if(result < 0):
        is_virtual = True
        result = result * (-1)
 
 
    if(is_virtual):
        x_real = -b / (2*a)
        x_virtual = math.sqrt(result)/(2*a)
        print("%.1f+%.1fi" %(x_real,x_virtual))
        print("%.1f-%.1fi" % (x_real, x_virtual))
    else:
        x_ans1 = (-b+math.sqrt(result))/(2*a)
        x_ans2 = (-b-math.sqrt(result))/(2*a)
        print("%.1f"%(x_ans1))
        print("%.1f"%(x_ans2))
 
 
 
a = int(input())
b = int(input())
c = int(input())
func(a, b, c)