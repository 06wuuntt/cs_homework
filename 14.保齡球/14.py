def getBall():
    ball1 = int(input())
    if ball1 != 10:
        ball2 = int(input())
        b = [ball1,ball2]
        ball.append(b)
    else:
        b = [ball1]
        ball.append(b)

def getPlus(l:list):
    for i in range(9):
        if l[i][0] == 10:
            plus.append(sum(l[i+1]))
        elif l[i][0] + l[i][1] == 10:
            plus.append(l[i+1][0])
            
def getExtra(l:list):
    if sum(l) == 10:
        if l[0] == 10:
            b1 = int(input())
            b2 = int(input())
            return b1+b2
        else:
            b1 = int(input())
            return b1
    else:
        return 0
        
ball = []
plus = []
total = 0
for i in range(10):
    getBall()
#print (ball)
getPlus(ball)
for i in ball:
    total+=sum(i)
print(total+sum(plus)+getExtra(ball[9]))