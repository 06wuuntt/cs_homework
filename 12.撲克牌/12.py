def getPoint(n):
    if n == 'A':
        return 0.5
    elif n == '1' or n == '2' or n == '3' or n == '4' or n == '5':
        return int(n)
    elif n == '6' or n == '7' or n == '8' or n == '9' or n == '10':
        return int(n)
    else:
        return 0.5
def getPlayerpoint(score):
    if score > 10.5:
        return 0
    else:
        return score
def rule1(c1,c2):
    player1 = getPlayerpoint(getPoint(c1[0]) + getPoint(c1[1]) + getPoint(c1[2]))
    player2 = getPlayerpoint(getPoint(c2[0]) + getPoint(c2[1]) + getPoint(c2[2]))
    if player1 == 0:
        print(f'{name2} Win')
    elif player1 > player2:
        print(f'{name1} Win')
    elif player1 < player2:
        print(f'{name2} Win')
    else:
        print('Tie')
def rule2(c1,c2):
    player1 = getPlayerpoint(getPoint(c1[0]) + getPoint(c1[1]) + getPoint(c1[2]))
    player2 = getPlayerpoint(getPoint(c2[0]) + getPoint(c2[1]) + getPoint(c2[2]))
    if player1 > player2:
        print(f'{name1} Win')
    elif player1 < player2:
        print(f'{name2} Win')
    else:
        print('Tie')
name1 = input()
card1 = []
for i in range(3):
    card1.append(input())
name2 = input()
card2 = []
for i in range(3):
    card2.append(input())

rule1(card1,card2)
rule2(card1,card2)