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

yMax = 0
xMax = 0
for d in dots:
    if d[0] > xMax:
        xMax = d[0]
    if d[1] > yMax:
        yMax = d[1]

yMax += 1
xMax += 1

print(yMax, xMax)

mat = numpy.empty((yMax, xMax), dtype=str)
for y in range(yMax):
    for x in range(xMax):
        mat[y, x] = "."

for d in dots:
    mat[d[1], d[0]] = "#"

for inst in instructions:
    print(inst)
    newMat = None
    if inst[0] == "x":
        newMat = numpy.ones((yMax, int(xMax / 2)), dtype=str)
        for y in range(yMax):
            for x in range(int(xMax / 2)):
                newMat[y, x] = "."
        for y in range(yMax):
            for x in range(0, inst[1]):
                a = xMax - 1 - x
                if mat[y, a] == "#" or mat[y, x] == "#":
                    newMat[y, x] = "#"
        xMax = int(xMax / 2)
    else:
        newMat = numpy.ones((int(yMax / 2), xMax), dtype=str)
        for y in range(int(yMax / 2)):
            for x in range(xMax):
                newMat[y, x] = "."
        for y in range(0, inst[1]):
            for x in range(xMax):
                a = yMax - 1 - y
                if mat[a, x] == "#" or mat[y, x] == "#":
                    newMat[y, x] = "#"
        yMax = int(yMax / 2)
    mat = newMat

    # print(mat)
    print(yMax, xMax)

print(mat)
