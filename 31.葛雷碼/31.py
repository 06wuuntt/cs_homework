def gray(n, k):
    if n == 1:
        print(k, end = '')
    elif k < 2**(n-1):
        print('0', end = '')
        gray(n-1, k)
    elif k >= 2**(n-1):
        print('1', end = '')
        gray(n-1, 2**n-1-k)

def main():
    alldata = list()
    while True:
        data = input()
        if data == '-1':
            break
        alldata.append(list(map(int, data.split())))
    for i in alldata:
        gray(i[0], i[1])
        print()

main()