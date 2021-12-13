import numpy

input = []

with open("day13_input.txt") as file:
    input = [line.strip() for line in file.readlines()]


isInstruction = False
dots = []
instructions = []
for i in input:
    if i == "":
        isInstruction = True
        continue
    if not isInstruction:
        parts = i.split(",")
        dots.append([int(parts[0]), int(parts[1])])
    else:
        parts = i.split("=")
        instructions.append([parts[0][-1], int(parts[1])])

yMax = max(d[1] for d in dots) + 1
xMax = max(d[0] for d in dots) + 1

mat = numpy.full((yMax, xMax), " ", dtype=str)

for d in dots:
    mat[d[1], d[0]] = "#"

for inst in instructions:
    newMat = None
    if inst[0] == "x":
        newMat = numpy.full((yMax, int(xMax / 2)), " ", dtype=str)
        for y in range(yMax):
            for x in range(0, inst[1]):
                if mat[y, xMax - 1 - x] == "#" or mat[y, x] == "#":
                    newMat[y, x] = "#"
        xMax = int(xMax / 2)
    else:
        newMat = numpy.full((int(yMax / 2), xMax), " ", dtype=str)
        for y in range(0, inst[1]):
            for x in range(xMax):
                if mat[yMax - 1 - y, x] == "#" or mat[y, x] == "#":
                    newMat[y, x] = "#"
        yMax = int(yMax / 2)
    mat = newMat

print(mat)
