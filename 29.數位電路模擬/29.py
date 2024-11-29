def turndecimal(l):
    for i in l:
        decimalnumber = int(i, 2)
        runtime(decimalnumber)

def runtime(number):
    count = 0
    while number != 1 and number != 0:
        if number%2 == 0:
            number /= 2
            count += 1
        else:
            number = (number+1)/2
            count += 1
    print(bin(count)[2:].zfill(4))

def main():
    alldata = list()
    while True:
        data = input()
        alldata.append(data)
        n = int(input())
        if n == -1:
            break
    turndecimal(alldata)

main()