import math
def getBookprice(l:list,price):
    if l[0]>=1 and l[0]<=10:
        return math.ceil(l[0]*price)
    elif l[0]>=11 and l[0]<=20:
        return math.ceil(l[0]*price*(l[1]/100))
    elif l[0]>=21 and l[0]<=30:
        return math.ceil(l[0]*price*(l[2]/100))
    elif l[0]>=31:
        return math.ceil(l[0]*price*(l[3]/100))

a_book = list(map(int,input().split(',')))
b_book = list(map(int,input().split(',')))
c_book = list(map(int,input().split(',')))
booklist = []
booklist.append([getBookprice(a_book,380),'A'])
booklist.append([getBookprice(b_book,1200),'B'])
booklist.append([getBookprice(c_book,180),'C'])
booklist = sorted(booklist,reverse=True)
for i in booklist:
    print(f'{i[1]},{i[0]}')
print(booklist[0][0]+booklist[1][0]+booklist[2][0])