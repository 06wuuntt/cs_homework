def check(str, d):
    l = {'{':1, '[':2, '(':3}
    r = {'}':-1, ']':-2, ')':-3}
    left = list()
    flag = True
    count = 0
    for i in str:
        if i in l:
            left.append(i)
            count += l[i]
        elif i in r:
            if len(left) == 0:
                flag = False
                break
            elif l[left[-1]] != abs(r[i]):
                flag = False
                break
            else:
                count += r[i]
                left.pop()
    if count != 0 or flag == False:
        print('fail')
    else:
        print('pass', end = ', ')
        grabstring(str, l, r, d)

def grabstring(str, left, right, depth):
    d = 0
    grab = ''
    for i in str:
        if i in left:
            d += 1
        elif i in right:
            d -= 1
        if d == depth and i.isalpha():
            grab += i
    if grab == '':
        print('EMPTY')
    else:
        print(grab)

def main():
    n, d = int(input()), int(input())
    string = list()

    for i in range(n):
        string.append(input())
    for i in string:
        check(i, d)
    
main()