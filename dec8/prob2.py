f = open("input1.txt", "r")


lines = []

for line in f:
    lines.append(line.strip())

f.close()
grid = []

for line in lines:
    row = []
    for i in range(len(line)):
        row.append(int(line[i]))
    grid.append(row)

# create a list containing scenic scores. All scores on edges are 0.

scores = []

for i in range(len(grid)):
    row = []
    for j in range(len(grid[i])):
        row.append(0)
    scores.append(row)


def getscore(lst, ref):
    copy = [lst[0]]
    if copy[0] >= ref:
        return 1
    for i in range(1, len(lst)):
        if lst[i] < ref:
            copy.append(lst[i])
        else:
            copy.append(10)
            return len(copy)
    return len(copy)


def getleftscore(row, column):
    sublst = []
    for i in range(column-1,-1,-1):
        sublst.append(grid[row][i])
    return getscore(sublst, grid[row][column])


def getrightscore(row, column):
    sublst = grid[row][column+1:]
    return getscore(sublst, grid[row][column])


def getabovescore(row, column):
    sublst = []
    for i in range(row-1,-1,-1):
        sublst.append(grid[i][column])
    return getscore(sublst, grid[row][column])


def getbelowscore(row, column):
    sublst = []
    for i in range(row+1,len(grid)):
        sublst.append(grid[i][column])
    return getscore(sublst, grid[row][column])


def addscore(row, column):
    return getleftscore(row, column)*getrightscore(row, column)*getabovescore(row, column)*getbelowscore(row, column)


for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        scores[i][j] = addscore(i,j)

maxscore = 0
for i in range(len(scores)):
    for j in range(len(scores[i])):
        if scores[i][j] >= maxscore:
            maxscore = scores[i][j]


print(maxscore)
