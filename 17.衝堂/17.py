def checkTime(l:list):
    for i in l:
        if i[0] <= '5' and i[0] >= '1':
            if i[1] >= '1' and i[1] <= '9':
                return True
            elif i[1] == 'a' or i[1] == 'b' or i[1] == 'c':
                return True
            else:
                return False
            
def checkHour(l:list):
    for i in l:
        if i[1] >= 1 and i[1] <= 3:
            return True
        else:
            return False
            



def main():
    courselist = []
    n = int(input())
    for i in range(n):
        coursedata = []
        coursename = str(input())
        coursedata.append(coursename)
        hour = int(input())
        for i in range(hour):
            time = str(input())
            coursedata.append(time)
        courselist.append(coursedata)
    for i in courselist:
        

main()