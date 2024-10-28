def getBMI(h,w):
    BMI = w/(h*h)
    return getRound(BMI)

def getRound(bmi):
    if (bmi*1000)%10 > 5:
        bmi += 0.01
    elif (bmi*1000)%10 == 5:
        if int(bmi*100)%2 == 1:
            bmi += 0.01
    bmi = int(bmi*100)/100
    return bmi

def getMaxandMin(bmilist:list):
    print(f'{max(bmilist):.2f}')
    print(f'{min(bmilist):.2f}')

def getMiddle(bmilist:list,n:int):
    bmilist = sorted(bmilist)
    if n%2 == 0:
        middle = round((bmilist[n//2-1]+bmilist[n//2])/2,3)
        print(f'{getRound(middle):.2f}')
    else:
        print(bmilist[n//2])

def getMost(bmilist:list):
    bmilist = sorted(bmilist,reverse = True)
    index = 0
    count = 0
    for i in bmilist:
        if bmilist.count(i) >= count:
            count = bmilist.count(i)
            index = bmilist.index(i)
    print(bmilist[index])

def main():
    BMIlist = []
    num = int(input())
    for i in range(num):
        height,weight = map(float,input().split(' '))
        BMIlist.append(getBMI(height,weight))
    #print(sorted(BMIlist))
    getMaxandMin(BMIlist)
    getMiddle(BMIlist,num)
    getMost(BMIlist)

main()