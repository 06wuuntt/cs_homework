def getValue(i, j, matrix):
    block = 0
    if i > 1:
        if j > 1:
            block = 4
        else:
            block = 3
    else:
        if j > 1:
            block = 2
        else:
            block = 1
    value = getrowset(i, matrix) & getcolset(j, matrix) & getblockset(block, matrix)
    if len(value) == 1:
        return value.pop()
    else:
        return 0
        
def getrowset(row, matrix):
    ans = {1, 2, 3, 4}
    compareset = set(matrix[row])
    return ans - compareset

def getcolset(col, matrix):
    ans = {1, 2, 3, 4}
    compareset = set()
    for i in range(4):
        compareset.add(matrix[i][col])
    return ans - compareset

def getblockset(block, matrix):
    ans = {1, 2, 3, 4}
    compareset = set()
    rowoffset = 0
    coloffset = 0
    if block == 1:
        pass
    elif block == 2:
        rowoffset = 2
    elif block == 3:
        coloffset = 2
    else:
        rowoffset = 2
        coloffset = 2
    compareset.add(matrix[0+coloffset][0+rowoffset])
    compareset.add(matrix[0+coloffset][1+rowoffset])
    compareset.add(matrix[1+coloffset][0+rowoffset])
    compareset.add(matrix[1+coloffset][1+rowoffset])
    return ans - compareset

def main():
    matrix = [[x for x in map(int, input().split())] for i in range(4)]
    zeronumber = sum([row.count(0) for row in matrix])
    while zeronumber > 0:
        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    value = getValue(i, j, matrix)
                    if value != 0:
                        matrix[i][j] = value
                        zeronumber -= 1
    for i in matrix:
        print(' '.join(map(str, i)))

main()