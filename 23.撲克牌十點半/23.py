def cardpoint(a):
    point = {str(a): a for a in range(2,11)}
    point.update({'A':1, 'J':0.5, 'Q':0.5, 'K':0.5})
    return point[a]

def getcardsum(l):
    return sum(cardpoint(i) for i in l)

def getfinalsum(s):
    if s > 10.5:
        return 0
    return s

def playerpluscard():
    flag = True
    x = input()
    if x == 'Y':
        playercard.append(input())
    elif x == 'N':
        flag = False
    if getcardsum(playercard) > 10.5:
        flag = False
    return flag

def computerpluscard():
    flag = True
    if getcardsum(computercard) <= 8 or getfinalsum(getcardsum(computercard)) <= getfinalsum(getcardsum(playercard)):
        computercard.append(input())
    if getcardsum(computercard) >= 8:
        flag = False
    return flag

def compare(p, c):
    computerscore = getfinalsum(getcardsum(c))
    playerscore = getfinalsum(getcardsum(p))
    if computerscore > playerscore:
        print('computer win')
    elif computerscore < playerscore:
        print('player win')
    else:
        print('it\'s a tie')

def main():
    playercard.append(input())
    computercard.append(input())
    pf, cf = True, True
    while pf or cf:
        if getcardsum(computercard) > 10.5:
             break
        if pf:
             pf = playerpluscard()
        if getcardsum(playercard) > 10.5:
            break
        if cf:
            cf = computerpluscard()
    compare(playercard, computercard)

playercard = list()
computercard = list()
main()