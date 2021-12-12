from typing import DefaultDict

input = []

with open("day12_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

nodes = DefaultDict(list)

for i in input:
    parts = i.split("-")
    nodes[parts[0]].append(parts[1])
    nodes[parts[1]].append(parts[0])


paths = []


def makePaths(currentPath, currentNode, smallVisited):
    currentPath.append(currentNode)

    if currentNode == "end":
        paths.append(currentPath)
        return

    for n in nodes[currentNode]:
        if n == "start":
            continue
        if n.isupper() or not n in currentPath:
            makePaths(currentPath[:], n, smallVisited)
        elif not smallVisited:
            makePaths(currentPath[:], n, True)


makePaths([], "start", True)
print(len(paths))

paths = []
makePaths([], "start", False)
print(len(paths))
