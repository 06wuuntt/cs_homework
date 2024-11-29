def Rtime(num):
    count = 0
    while num != 1 and num != 0:
        if num%2 == 0:
            num /= 2
            count += 1
        else:
            num = (num+1)/2
            count += 1
    return(count)

def Ttime(num):
    ans = 0
    for i in range(num+1):
        ans += Rtime(i)
    print(bin(ans)[2:].zfill(14))

def main():
    alldata = list()
    while True:
        data = input()
        if data == '-1':
            break
        alldata.append(int(data,2))
    for i in alldata:
        Ttime(i)

main()