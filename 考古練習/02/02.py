import math
def getBMI(h,w):
    bmi = (w*0.454)/(h/100)**2
    bmi = math.floor(bmi*100)/100
    if bmi >= 18.5 and bmi <= 24:
        return f'{bmi:.2f}'
    elif bmi >= 24:
        return 'BMI too high'
    else:
        return 'BMI too low'

def check(l):
    for i in l:
        if i[0] < 50 or i[0] > 250:
            print('Input Height Error')
        elif i[1] < 20 or i[1] > 300:
            print('Input Weight Error')
        else:
            print(getBMI(i[0], i[1]))


def main():
    peopledata = list()
    while True:
        x = input()
        if x == '-1':
            break
        else:
            people = list(map(int, x.split()))
            peopledata.append(people)
    check(peopledata)
    
if __name__ == '__main__':
    main()