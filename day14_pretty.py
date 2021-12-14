from typing import DefaultDict

input = []

with open("day14_input.txt") as file:
    input = [line.strip() for line in file.readlines()]


polymer = input.pop(0)

# skip empty line
input.pop(0)

instructions = {p[0]: p[1] for p in map(lambda i: i.split(" -> "), input)}

polyPairs = DefaultDict(int)

for j in range(len(polymer) - 1):
    polyPairs[polymer[j] + polymer[j + 1]] += 1


letterCounts = DefaultDict(int)

for l in polymer:
    letterCounts[l] += 1


def doProcess(xTimes, polyPairs):
    for _ in range(xTimes):
        newDict = DefaultDict(int)
        for p in polyPairs.keys():
            if p in instructions:
                newDict[p[0] + instructions[p]] += polyPairs[p]
                newDict[instructions[p] + p[1]] += polyPairs[p]
                letterCounts[instructions[p]] += polyPairs[p]
            else:
                newDict[p] = polyPairs[p]

        polyPairs = newDict

    lMax = max(letterCounts.values())
    lMin = min(letterCounts.values())

    print(lMax - lMin)


doProcess(10, polyPairs)
doProcess(30, polyPairs)
