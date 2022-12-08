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

# create a list where 1 marks a visible tree and 0 otherwise

visible = []

for i in range(len(grid)):
    row = []
    for j in range(len(grid[i])):
        row.append(0)
    visible.append(row)

## All trees on the edge are visible

for i in range(len(visible[0])):
    visible[0][i] = 1
    visible[-1][i] = 1

for i in range(len(visible)):
    visible[i][0] = 1
    visible[i][-1] = 1

def isvisible(row, column):
    refvalue = grid[row][column]
    isvisible = 0
    if max(grid[row][:column]) < refvalue:
        isvisible = 1
    if max(grid[row][column+1:]) < refvalue:
        isvisible = 1
    colup = []
    coldown = []
    for i in range(len(grid)):
        if i < row:
            colup.append(grid[i][column])
        elif i > row:
            coldown.append(grid[i][column])
    if max(colup) < refvalue:
        isvisible = 1
    if max(coldown) < refvalue:
        isvisible = 1
    visible[row][column] = isvisible


for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        isvisible(i,j)

counter = 0
for i in range(len(visible)):
    for j in range(len(visible[i])):
        if visible[i][j] == 1:
            counter += 1

print(counter)
