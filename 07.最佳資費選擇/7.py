def getMoney183(a,b,c,d,e,f):
    total = a*0.08 + b*0.139 + c*0.135 + d*1.128 + e*1.483
    if f>1:
        total += (f-1)*250
    if total >= 183:
        return total
    else:
        return 183
def getMoney383(a,b,c,d,e,f):
    total = a*0.07 + b*0.13 + c*0.121 + d*1.128 + e*1.483
    if f>3:
        total += (f-3)*200
    if total >= 383:
        return total
    else:
        return 383
def getMoney983(a,b,c,d,e,f):
    total = a*0.06 + b*0.108 + c*0.101 + d*1.128 + e*1.483
    if f>5:
        total += (f-5)*150
    if total >= 983:
        return total
    else:
        return 983 
def getMoney1283(a,b,c,d,e,f):
    total = a*0.05 + b*0.1 + c*0.09 + d*1.128 + e*1.483
    if total >= 1283:
        return total
    else:
        return 1283
def main():
    incall,outcall,homecall,inmessage,outmessage,internet = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
    moneylist = []
    moneylist.append(getMoney183(incall,outcall,homecall,inmessage,outmessage,internet))
    moneylist.append(getMoney383(incall,outcall,homecall,inmessage,outmessage,internet))
    moneylist.append(getMoney983(incall,outcall,homecall,inmessage,outmessage,internet))
    moneylist.append(getMoney1283(incall,outcall,homecall,inmessage,outmessage,internet))
    print(round(min(moneylist)))
    
    listindex = moneylist.index(min(moneylist))
    if listindex == 0:
        print('183')
    elif listindex == 1:
        print('383')
    elif listindex == 2:
        print('983')
    elif listindex == 3:
        print('1283')            
main()