
input = []

with open("day9_input.txt") as file:
    input = [line.strip()
             for line in file.readlines()]

xMax = len(input[0])
yMax = len(input)

c = 0

for y in range(yMax):
    for x in range(xMax):
        # up
        if y != 0 and input[y][x] >= input[y-1][x]:
            continue
        # down
        if y != yMax - 1 and input[y][x] >= input[y+1][x]:
            continue
        # right
        if x != xMax - 1 and input[y][x] >= input[y][x+1]:
            continue
        # left
        if x != 0 and input[y][x] >= input[y][x-1]:
            continue

        c += int(input[y][x]) + 1

print(c)


input = list(
    map(lambda x: list(map(lambda y: y == "9", x)), input))


def fillBasin(x, y, cnt):
    if input[y][x]:
        return cnt

    input[y][x] = True
    q = cnt + 1
    if x != 0:
        q += fillBasin(x-1, y, 0)
    if x != xMax-1:
        q += fillBasin(x+1, y, 0)
    if y != 0:
        q += fillBasin(x, y-1, 0)
    if y != yMax-1:
        q += fillBasin(x, y+1, 0)

    return q


maxs = []
for y in range(yMax):
    for x in range(xMax):
        maxs.append(fillBasin(x, y, 0))

asd = sorted(maxs)
asd.reverse()
print(asd[0] * asd[1] * asd[2])
