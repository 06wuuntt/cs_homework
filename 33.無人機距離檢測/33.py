import math
def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return d

def main():
    n = int(input())
    location = list()
    alldistance = list()
    for i in range(n):
        a, x, y, z = map(int, input().split())
        location.append([x, y, z])
    for i in range(0, n):
        for j in range(i+1, n):
            d = distance(location[i][0], location[i][1], location[i][2], location[j][0], location[j][1], location[j][2])
            alldistance.append([d, i, j])
    alldistance.sort()
    for i in range(3):
        print(f'{alldistance[i][1]+1} {alldistance[i][2]+1}', end = ' ')
        print(' '.join(map(str, location[alldistance[i][1]])),end = ' ')
        print(' '.join(map(str, location[alldistance[i][2]])))
main()