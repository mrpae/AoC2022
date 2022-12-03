### A - Rock
### B - Paper
### C - Scissors
### X - Rock
### Y - Paper
### Z - Scissors

f = open("input1.txt", "r")
games = []
score = 0

for line in f:
    games.append(line.strip().split(" "))

f.close()


for game in games:
    if game[1] == "X":
        if game[0] == "A":
            score += 1 + 3
        elif game[0] == "B":
            score += 1 + 0
        elif game[0] == "C":
            score += 1 + 6
    elif game[1] == "Y":
        if game[0] == "A":
            score += 2 + 6
        elif game[0] == "B":
            score += 2 + 3
        elif game[0] == "C":
            score += 2 + 0
    elif game[1] == "Z":
        if game[0] == "A":
            score += 3 + 0
        elif game[0] == "B":
            score += 3 + 6
        elif game[0] == "C":
            score += 3 + 3

print(score)
