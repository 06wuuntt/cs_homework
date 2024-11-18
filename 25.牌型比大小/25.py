def getcardnumber(a):
    cardnumber = {str(i):i for i in range(2,11)}
    cardnumber.update({'A':1, 'J':11, 'Q':12, 'K':13})
    return cardnumber[a]

def splitcolornumber(l):
    flag = True
    c, n = list(), list()
    for i in l:
        if len(i) >= 3:
            if i[1] == '1' and i[2] == '0':
                n.append(10)
                c.append(i[0])
            else:
                flag = False
        else:
            n.append(getcardnumber(i[1]))
            c.append(i[0])
    numberlist.append(n)
    colorlist.append(c)    
    return flag

def checkcorrect(i):
    flag = True
    if i == 1:    #checkcolor
        c = [item for l in colorlist for item in l]
        flag = all(item in ['S', 'H', 'D', 'C'] for item in c)
    elif i == 0:  #checknumber
        n = [item for l in numberlist for item in l]
        flag = all(item >= 1 and item <= 13 for item in n)
    return flag

def continuecard(n):
    allcard = list()
    for i in range(1,14):
        seq = [i+n if i+n <= 13 else i+n-13 for n in range(0,5)]
        seq.sort()
        allcard.append(seq)
    return n in allcard

def getcardpoint(number, color):
    number.sort()
    if continuecard(number):
        if len(set(color)) == 1:
            return 9
        else:
            return 5
    elif len(set(number)) == 2:
        if number.count(number[0]) == 1 or number.count(number[4]) == 1:
            return 8
        elif number.count(number[0]) == 2 or number.count(number[4]) == 2:
            return 7
    elif len(set(color)) == 1:
        return 6
    elif len(set(number)) == 3:
        newnumber = list(set(number))
        if number.count(newnumber[0]) == 3 or number.count(newnumber[1]) == 3 or number.count(newnumber[2]) == 3:
            return 4
        else:
            return 3
    elif len(set(number)) == 4:
        return 2
    else:
        return 1
    
def main():
    A_card = input().split()
    B_card = input().split()
    desk_card = input().split()
    allcard = A_card + B_card + desk_card
    if splitcolornumber(A_card) == False or splitcolornumber(B_card) == False or splitcolornumber(desk_card) == False:
        print('Error input')
    elif checkcorrect(1) == False or checkcorrect(0) == False:
        print('Error input')
    elif len(allcard) != len(set(allcard)):
        print('Duplicate deal')
    else:
        A_take_card = [[A_card[0]]+desk_card, [A_card[1]]+desk_card]
        B_take_card = [[B_card[0]]+desk_card, [B_card[1]]+desk_card]
        for i in range(2):
            card = [desk_card[i],desk_card[i+1],desk_card[i+2]]
            A_take_card.append(A_card+card)
            B_take_card.append(B_card+card)
        A_take_card.extend([A_card + [desk_card[2], desk_card[3], desk_card[0]]])
        A_take_card.extend([A_card + [desk_card[3], desk_card[0], desk_card[1]]])
        B_take_card.extend([B_card + [desk_card[2], desk_card[3], desk_card[0]]])
        B_take_card.extend([B_card + [desk_card[3], desk_card[0], desk_card[1]]])
        A_score, B_score = 0, 0       
        for i in A_take_card:
            c, n = list(), list()
            for j in i:
                if len(j) == 3:
                    n.append(10)
                else:
                    n.append(getcardnumber(j[1]))
                c.append(j[0])
            if getcardpoint(n, c) > A_score:
                A_score = getcardpoint(n, c)
        for i in B_take_card:
            c, n = list(), list()
            for j in i:
                if len(j) == 3:
                    n.append(10)
                else:
                    n.append(getcardnumber(j[1]))
                c.append(j[0])
            if getcardpoint(n, c) > B_score:
                B_score = getcardpoint(n, c)
        if A_score > B_score:
            print(f'A {A_score}')
        elif B_score > A_score:
            print(f'B {B_score}')
        else:
            print('Tie')

numberlist = list()
colorlist = list()
main()