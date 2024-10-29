def checktime(l):
    for i in range(2,l[1]+2):
        if l[i][0] <= '5' and l[i][0] >= '1':
            if l[i][1] >= '1' and l[i][1] <= '9':
                continue
            elif l[i][1] == 'a' or l[i][1] == 'b' or l[i][1] == 'c':
                continue
            else:
                return False
        else:
            return False

def checkhour(hour):
    if hour <= 3 and hour >= 1:
        return True
    else:
        return False
    
def isConflict(l, n):
    b = True
    for i in l[2:l[1]+2]:
        for j in range(coursedata.index(l)+1,n):
            if i in coursedata[j]:
                print(f'{l[0]},{coursedata[j][0]},{i}')
                b = False
    return b

def writeCourse():
    coursename = input()
    coursehour = int(input())
    course = [coursename, coursehour]
    for i in range(coursehour):
        time = input()
        course.append(time)
    coursedata.append(course)

def main():
    conflictflag = True 
    flag = True
    n = int(input())
    for i in range(n):
        writeCourse()
    for i in coursedata:
        if checktime(i) == False or checkhour(i[1]) == False:
            print('-1')
            conflictflag = False
            flag = False
            break
    if flag:
        for i in coursedata:
            a = isConflict(i, n)
            if a == False:
                conflictflag = False

    if conflictflag:
        print('correct')

coursedata = list()
main()