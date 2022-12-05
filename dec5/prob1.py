####################################
#####                          #####
#####    Data preprocessing    #####
#####                          #####
####################################

f = open("input1.txt", "r")

# Since the stacks are relatively simple, then it's much easier to
# define the stacks as a dictonary, rather than to read the information
# from the input file.

stacks = {1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
          2: ["G", "W", "F", "C", "B", "S", "T", "V"],
          3: ["C", "B", "S", "N", "W"],
          4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
          5: ["T", "S", "L", "F", "D", "H", "B"],
          6: ["J", "V", "T", "W", "M", "N"],
          7: ["P", "F", "L", "C", "S", "T", "G"],
          8: ["B", "D", "Z"],
          9: ["M", "N", "Z", "W"]}

lines = []

for line in f:
    lines.append(line.strip())

commands = lines[10:]    # this list contains all the necessary commands

f.close()

####################################
#####                          #####
#####   Necessary functions    #####
#####                          #####
####################################


def move(src, dest):
    global stacks
    value = stacks[src].pop()
    stacks[dest].append(value)


def executecommand(command):
    data = command.split(" ")[1::2]
    for i in range(int(data[0])):
        move(int(data[1]), int(data[2]))


def printoutput():
    global stacks
    output = ""
    for i in range(1,10):
        output += stacks[i][-1]
    print(output)


for command in commands:
    executecommand(command)

printoutput()
