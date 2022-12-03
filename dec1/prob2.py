f = open("input1.txt", "r")

calories = []

lst = []

for line in f:
    linedata = line.strip()
    if linedata == "":
        calories.append(lst)
        lst = []
    else:
        lst.append(int(linedata))

f.close()

elfcalories = []
for elem in calories:
    elfcalories.append(sum(elem))

elfcalories.sort(reverse=True)

print(sum(elfcalories[:3]))
