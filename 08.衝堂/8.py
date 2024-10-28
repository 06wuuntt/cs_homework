def checktime(course_time:list):
    for i in course_time:
        if i[0]>='1' and i[0]<='5':
            if i[1] >='1' and i[1] <= '9':
                return True
            elif i[1] == 'a' or i[1] == 'b' or i[1] =='c':
                return True
            else:
                return False
        else:
            return False
def checkhour(hour):
    if hour <= 3 and hour >= 1:
        return True
    else:
        return False
def checkconflict(course1,course2,course3):
    isConflict = False
    for i in course1:
        for j in course2:
            if i == j:
                print(f'{course1_id},{course2_id},{i}')
                isConflict = True
    
    for i in course1:
        for j in course3:
            if i == j:
                print(f'{course1_id},{course3_id},{i}')  
                isConflict = True
    for i in course2:
        for j in course3:
            if i == j:
                print(f'{course2_id},{course3_id},{i}')
                isConflict = True
                
    if isConflict == False:
        print('correct')

course1_id = input()
course1_hour = int(input())
course1_time = []
for i in range(course1_hour):
    course1_time.append(input())
    
course2_id = input()
course2_hour = int(input())
course2_time = []
for i in range(course2_hour):
    course2_time.append(input())
    
course3_id = input()
course3_hour = int(input())
course3_time = []
for i in range(course3_hour):
    course3_time.append(input())
if checktime(course1_time) and checktime(course2_time) and checktime(course3_time):
    if checkhour(course1_hour) and checkhour(course2_hour) and checkhour(course3_hour):
        checkconflict(course1_time,course2_time,course3_time)
    else:
        print('-1')
else:
    print('-1')