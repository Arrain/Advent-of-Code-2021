import numpy
input = []

with open("day11_input.txt") as file:
    input = [list(map(lambda x: int(x), line.strip()))
             for line in file.readlines()]

octoMap = numpy.pad(numpy.asmatrix(input), 1,
                    "constant", constant_values=(9, 9))
yMax = octoMap.shape[0]
xMax = octoMap.shape[1]

c = 0
i = -1
while True:
    i += 1
    if i == 100:
        print(c)

    freshMap = numpy.ones((yMax, xMax), dtype=bool)

    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            octoMap[y, x] += 1

    while True:
        flashHappened = False
        for y in range(1, yMax-1):
            for x in range(1, xMax-1):
                if octoMap[y, x] > 9 and freshMap[y, x]:
                    c += 1
                    flashHappened = True

                    freshMap[y, x] = False
                    octoMap[y, x] = 0

                    octoMap[y-1, x-1] += 1
                    octoMap[y-1, x] += 1
                    octoMap[y-1, x+1] += 1
                    octoMap[y, x-1] += 1
                    octoMap[y, x+1] += 1
                    octoMap[y+1, x-1] += 1
                    octoMap[y+1, x] += 1
                    octoMap[y+1, x+1] += 1

        if not flashHappened:
            break

    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            if freshMap[y, x] == False:
                octoMap[y, x] = 0

    isFin = True
    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            if freshMap[y, x] == True:
                isFin = False

    if isFin:
        print(i+1)
        break
