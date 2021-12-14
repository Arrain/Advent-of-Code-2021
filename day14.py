import string, sys
from typing import DefaultDict

input = []

with open("day14_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

polymer = input.pop(0)

input.pop(0)

instr = {}
for i in input:
    parts = i.split(" -> ")
    instr[parts[0]] = parts[1]


polyPairs = DefaultDict(int)

for j in range(len(polymer) - 1):
    polyPairs[polymer[j] + polymer[j + 1]] += 1

letters = DefaultDict(int)
for l in polymer:
    letters[l] += 1

for i in range(40):
    keys = list(polyPairs.keys())
    newDict = DefaultDict(int)
    for p in keys:
        if p in instr:
            val = polyPairs[p]
            newDict[p[0] + instr[p]] += val
            newDict[instr[p] + p[1]] += val
            letters[instr[p]] += val
        else:
            newDict[p] = polyPairs[p]

    polyPairs = newDict


lMax = 0
lMin = sys.maxsize

for letter in letters.keys():
    q = letters[letter]
    if q != 0:
        if q > lMax:
            lMax = q
        if q < lMin:
            lMin = q

print(lMax - lMin)
