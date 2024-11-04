def isConflict(l):
    for i in range(allcourse.index(l)+1, len(allcourse)):
        for j in range(2, l[1]+2):
            if l[j] in allcourse[i]:
                print(f'{l[0]} and {allcourse[i][0]} conflict on {l[j]}')

def main():
    n = int(input())
    for i in range(n):
        course = list()
        name, hour = input(), int(input())
        course.extend([name, hour])
        for i in range(hour):
            course.append(input())   #course time
        allcourse.append(course)
    for i in allcourse:
        isConflict(i)
    
allcourse = list()
main()