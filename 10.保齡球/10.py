def getninthscore():
    ninth1 = int(input())
    if ninth1 == 10:
        return 10
    else:
        ninth2 = int(input())
        if ninth1 + ninth2 == 10:
            return 10 + 10
        else:
            return ninth1 + ninth2
    
def gettenthscore():
    tenth1 = int(input())
    if tenth1 == 10:
        return 10 + getextrascore(2)
    else:
        tenth2 = int(input())
        if tenth1 + tenth2 == 10:
            return 10 + getextrascore(1)
        else:
            return tenth1 + tenth2
        
def getextrascore(n:int):
    extrasum = 0
    for i in range(n):
        extrasum += int(input())
    return extrasum

total = getninthscore() + gettenthscore()
print(total)