f = open("input1.txt", "r")

pairs = []
counter = 0

for line in f:
    elves = line.strip().split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    pairs.append([int(elf1[0]), int(elf1[1]), int(elf2[0]), int(elf2[1])])

f.close()

for pair in pairs:
    smallest = min(pair)
    largest = max(pair)
    if (largest - smallest - 1 < pair[1] - pair[0] + pair[3] - pair[2]):
        counter += 1

print(counter)

