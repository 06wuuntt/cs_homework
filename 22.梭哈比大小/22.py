def getnumber(a):
    cardnumber = {str(n) : n for n in range(2, 11)}
    cardnumber.update({'A':1, 'J':11, 'Q':12, 'K':13})
    return cardnumber[a]

def checknumber(l):
    flag = True
    for i in l:
        flag = all(1 <= j <= 13 for j in i)
        if flag == False:
            break
    return flag

def checkcolor(l):
    flag = True
    for i in l:
        flag = all(j in ['S', 'H', 'D', 'C'] for j in i)
        if flag == False:
            break
    return flag

def checkduplicate(l):
    allcard = [item for card in l for item in card]
    return len(allcard) == len(set(allcard))

def splitnumbercolor(l):
    flag = True
    for i in l:
        cardnumber = list()
        cardcolor = list()
        number = [str(a) for a in range(2,10)]
        number.extend(['A','J','Q','K'])
        for j in range(1,6):
            if len(i[j]) >= 3:
                if i[j][0] == '1' and i[j][1] == '0':
                    cardnumber.append(10)
                    cardcolor.append(i[j][2])
                else:
                    flag = False
            elif (i[j][0] in number) == False:
                flag = False
                break
            else:
                cardnumber.append(getnumber(i[j][0]))
                cardcolor.append(i[j][1])
        cardnumbers.append(cardnumber)
        cardcolors.append(cardcolor)
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

def getpeoplepoint(number, color, allcard):
    for i in range(0, len(allcard)):
        point = list()
        point.append(getcardpoint(number[i],color[i]))
        point.append(allcard[i][0])
        points.append(point)
    points.sort(reverse = True)
    for i in points:
        print(f'{i[1]} {i[0]}')

def main():
    n = int(input())
    for i in range(n):
        card = input().split()
        cards.append(card)
    if splitnumbercolor(cards) == False or checkcolor(cardcolors) == False or checknumber(cardnumbers) == False:
        print('Error input')
    elif checkduplicate(cards) == False:
        print('Duplicate deal')
    else:
        getpeoplepoint(cardnumbers, cardcolors, cards)

cards = list()
cardnumbers = list()
cardcolors = list()
points = list()
main()