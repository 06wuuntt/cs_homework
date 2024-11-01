def getcardnumber(a):           # 將牌面轉換成數字
    cardnumber = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
    return cardnumber[a]

def splitnumbercolor(l):        # 分開數字和花色
    flag = True
    for i in l:
        if len(i) >= 3:
            if i[0] == '1' and i[1] == '0':
                cardnumber.append(10)
                cardcolor.append(i[2])
            else:
                flag = False
        else:
            cardnumber.append(getcardnumber(i[0]))
            cardcolor.append(i[1])
    return flag

def checknumber(l):             # 確認數字是否符合範圍
    flag = True
    for i in l:
        if i > 13 or i < 1:
            flag = False
    return flag

def checkcolor(l):              # 確認花色是否為那四個
    flag = True
    for i in l:
        if i != 'S' and i != 'H' and i != 'D' and i != 'C':
            flag = False
    return flag

def checkduplicate(l):          # 確認是否有重複的牌
    return len(l) == len(set(l))
        
def continuecard(l):            # 判斷數字是否連續
    flag = True
    if 1 in l and 13 in l:
        l[l.index(1)] = 14
        if 2 in l:
            l[l.index(2)] = 15
            if 3 in l:
                l[l.index(3)] = 16
                if 4 in l:
                    l[l.index(4)] = 17
    l.sort()
    for i in range(len(l)-1):
        if l[i+1] - l[i] != 1:
            flag = False
    return flag

def othercard(color,number):      # 檢查牌面大小
    number = sorted(number)
    if continuecard(number):
        if len(set(color)) == 1:
            print('9')            # straight flush (9)
        else:
            print('5')            # straight (5)
    elif len(set(number)) == 2:
        if number.count(number[0]) == 1 or number.count(number[4]) == 1:
            print('8')            # Four of a kind (8)
        elif number.count(number[0]) == 2 or number.count(number[4]) == 2:
            print('7')            # Full house (7)
    elif len(set(color)) == 1:
        print('6')                # Flush (6)
    elif len(set(number)) == 3:
        newnumber = list(set(number))
        if number.count(newnumber[0]) == 3 or number.count(newnumber[1]) == 3 or number.count(newnumber[2]) == 3:
            print('4')            # Three of a kind (4)
        else:
            print('3')            # Two pairs (3)
    elif len(set(number)) == 4:
        print('2')                # One pair (2)
    else:   
        print('1')                # High card (1)

def main():
    card = list(map(str, input().split(' ')))
    checklenflag = splitnumbercolor(card)
    if checklenflag == False or checkcolor(cardcolor) == False or checknumber(cardnumber) == False:
        print('Error input')
    elif checkduplicate(card) == False:
        print('Duplicate deal')
    else:
        othercard(cardcolor, cardnumber)
  
cardnumber = list()
cardcolor = list()
main()