import sys
from heapq import heappop, heappush
from typing import DefaultDict

input = []

with open("day15_input.txt") as file:
    input = {
        (y, x): int(r)
        for y, row in enumerate(file.readlines())
        for x, r in enumerate(row.strip())
    }

size = max(i[0] for i in input) + 1

transX = [0, 0, -1, 1]
transY = [-1, 1, 0, 0]


def doSmallPath(input, size):
    dist = DefaultDict(lambda: sys.maxsize, {(0, 0): 0})
    q = []
    for i in input:
        heappush(q, (dist[i], i))

    while len(q) > 0:
        curr = heappop(q)[1]
        if curr == (size - 1, size - 1):
            print(dist[curr])
            break
        for i in range(4):
            next = (transY[i] + curr[0], transX[i] + curr[1])
            alt = dist[curr] + input.get(next, sys.maxsize)
            if alt < dist[next]:
                dist[next] = alt
                heappush(q, (dist[next], next))


doSmallPath(input, size)

newInput = input.copy()
for i in input:
    for yn in range(5):
        for xn in range(5):
            newInput[(yn * size + i[0], xn * size + i[1])] = (
                input[i] + yn + xn - 1
            ) % 9 + 1

doSmallPath(newInput, size * 5)
