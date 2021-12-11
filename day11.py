import numpy
input = []

with open("day11_input.txt") as file:
    input = [list(map(lambda x: int(x), line.strip()))
             for line in file.readlines()]

hMap = numpy.pad(numpy.asmatrix(input), 1, "constant", constant_values=(9, 9))
yMax = hMap.shape[0]
xMax = hMap.shape[1]

usedMap = numpy.pad(numpy.asmatrix(input), 1,
                    "constant", constant_values=(9, 9))

c = 0
i = -1
while True:
    i += 1
    if i == 100:
        print(c)
    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            hMap[y, x] += 1
    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            usedMap[y, x] = True
    flashHap = True
    while flashHap:
        flashHap = False
        for y in range(1, yMax-1):
            for x in range(1, xMax-1):
                if hMap[y, x] > 9 and usedMap[y, x]:
                    usedMap[y, x] = False
                    c += 1
                    hMap[y, x] = 0
                    flashHap = True
                    hMap[y-1, x-1] += 1
                    hMap[y-1, x] += 1
                    hMap[y-1, x+1] += 1
                    hMap[y, x-1] += 1
                    hMap[y, x+1] += 1
                    hMap[y+1, x-1] += 1
                    hMap[y+1, x] += 1
                    hMap[y+1, x+1] += 1
    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            if usedMap[y, x] == False:
                hMap[y, x] = 0
    isFin = True
    for y in range(1, yMax-1):
        for x in range(1, xMax-1):
            if usedMap[y, x] == True:
                isFin = False

    if isFin:
        break

print(i+1)
