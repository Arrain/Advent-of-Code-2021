import numpy
input = []

with open("day9_input.txt") as file:
    input = [list(map(lambda x: int(x), line.strip()))
             for line in file.readlines()]

hMap = numpy.pad(numpy.asmatrix(input), 1, "constant", constant_values=(9, 9))
yMax = hMap.shape[0]
xMax = hMap.shape[1]

c = 0

for y in range(1, yMax-1):
    for x in range(1, xMax-1):
        # up
        if (hMap[y, x] >= hMap[y-1, x] or
                hMap[y, x] >= hMap[y+1, x] or
                hMap[y, x] >= hMap[y, x+1] or
                hMap[y, x] >= hMap[y, x-1]):
            continue

        c += hMap[y, x] + 1

print(c)


def fillBasin(x, y, cnt):
    if hMap[y, x] == 9:
        return cnt

    hMap[y, x] = 9
    q = cnt + 1
    q += fillBasin(x-1, y, 0)
    q += fillBasin(x+1, y, 0)
    q += fillBasin(x, y-1, 0)
    q += fillBasin(x, y+1, 0)

    return q


maxs = []
for y in range(yMax):
    for x in range(xMax):
        maxs.append(fillBasin(x, y, 0))

maxs = sorted(maxs)
maxs.reverse()
print(maxs[0] * maxs[1] * maxs[2])
