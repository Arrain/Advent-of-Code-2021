input = []

with open("day12_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

nodes = {}

for i in input:
    parts = i.split("-")
    if parts[0] in nodes:
        nodes[parts[0]].append(parts[1])
    else:
        nodes[parts[0]] = [parts[1]]
    if parts[1] in nodes:
        nodes[parts[1]].append(parts[0])
    else:
        nodes[parts[1]] = [parts[0]]

paths = []


def makePaths(path, cn, smallVis):
    path.append(cn)
    if cn == "end":
        paths.append(path)
        return path

    for i in nodes[cn]:
        if i == "start":
            continue
        if i.isupper():
            makePaths(path[:], i, smallVis)
        else:
            if not i in path:
                makePaths(path[:], i, smallVis)
            else:
                if not smallVis:
                    makePaths(path[:], i, True)


makePaths([], "start", True)
print(len(paths))

paths = []
makePaths([], "start", False)
print(len(paths))
