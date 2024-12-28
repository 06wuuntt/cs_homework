def getUniversity():
    university = dict()
    n = int(input())
    for i in range(n):
        universitycon = input().split()
        university[universitycon[0]] = set(universitycon[1:])
    return university

def compare0(university, con):
    condition = con.split(' + ')
    condition = [set(i.split(' ')) for i in condition]
    for i in university:
        for j in condition:
            if university[i].issuperset(j):
                print(i, end = ' ')
                break
    print('')

def compare1(university, con):
    con = con.replace(' + ', ' ')
    con = set(con.split(' '))
    max = 0
    allcorrect = dict()
    for i in university:
        correct = con & university[i]
        if len(correct) > max:
            max = len(correct)
        allcorrect.update({i:correct})
    for i in allcorrect:
        if len(allcorrect[i]) == max:
            print(i, end = ' ')
    print('')


def main():
    university = getUniversity()
    n = int(input())
    condition = list()
    for i in range(n):
        con = input()
        condition.append(con)
    d = int(input())
    if d == 0:
        for i in condition:
            compare0(university, i)
    elif d == 1:
        for i in condition:
            compare1(university, i)

main()