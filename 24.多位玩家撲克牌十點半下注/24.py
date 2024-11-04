def getpoint(i):
    cardpoint = {str(a):a for a in range(2,11)}
    cardpoint.update({'A':1, 'J':0.5, 'Q':0.5, 'K':0.5})
    return cardpoint[i]

def getcardsum(l):
    total = sum(getpoint(l[i]) for i in range(0, len(l)))
    return total

def getfinalsum(s):
    if s > 10.5:
        return 0
    else:
        return s

def playerpluscard(x, i):
    plus, num = x.split(' ')
    playerscard[i].append(num)

def computerpluscard():
    playerscard[0].append(input())

def main():
    money = list(map(int, input().split()))
    firstcard = input().split()
    for i in firstcard:
        playerscard.append([i])
    for i in range(1, n+1):
        while True:
            x = input()
            if x == 'N':
                break
            else:
                playerpluscard(x, i)
            if getcardsum(playerscard[i]) > 10.5:
                result[i] = (-1)*money[i-1]
                break
            elif getcardsum(playerscard[i]) == 10.5:
                result[i] = money[i-1]
                break
    while True:
        if getcardsum(playerscard[0]) <= min(getcardsum(playerscard[a]) for a in range(1, n+1)) and all(getcardsum(playerscard[a]) >= 10.5 for a in range(1, n+1)) == False:
            computerpluscard()
        else:
            break
        if getcardsum(playerscard[0]) > 10.5:
            break
        elif getcardsum(playerscard[0]) == 10.5:
            break
    for i in range(1, n+1):
        if result[i] == 0:
            if getfinalsum(getcardsum(playerscard[i])) <= getfinalsum(getcardsum(playerscard[0])):
                result[i] = (-1)*money[i-1]
            else:
                result[i] = money[i-1]
    result[0] = (-1)*sum(result[a] for a in range(1, n+1))
    for i in range(1,n+1):
        if result[i] > 0:
            print(f'Player{i} +{result[i]}')
        else:
            print(f'Player{i} {result[i]}')
    if result[0] > 0:
        print(f'Computer +{result[0]}')
    else:
        print(f'Computer {result[0]}')

n = int(input())
result = [0]*(n+1)
playerscard = list()
main()