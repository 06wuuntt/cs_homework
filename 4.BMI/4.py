import math
def BMI (h,w):
    ans = w/(h*h)
    return ans

height = eval(input())
weight = eval(input())
bmi = BMI(height,weight)
bmistr = str(bmi)
if (bmistr[5]=='5'):
    a = int(bmistr[4])
    if (a%2 == 0):
        print(math.floor(bmi*100)/100.0)
    else:
        print("{:.2f}".format(round(bmi,2)))
else:
    print("{:.2f}".format(round(bmi,2)))