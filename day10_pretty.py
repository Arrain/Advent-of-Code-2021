
input = []

with open("day10_input.txt") as file:
    input = [line.strip()
             for line in file.readlines()]

costs = {")": 3, "]": 57, "}": 1197, ">": 25137}


def redPar(val):
    l = 0
    while l != len(val):
        l = len(val)
        val = val.replace("()", "")
        val = val.replace("[]", "")
        val = val.replace("{}", "")
        val = val.replace("<>", "")

    return val


s = 0
incompleteLines = []
for line in input:
    oldS = s
    line = redPar(line)
    last = line[0]
    for j in range(1, len(line)):
        if ((line[j] == ")" and last != "(") or
                (line[j] == "]" and last != "[") or
                (line[j] == "}" and last != "{") or
                (line[j] == ">" and last != "<")):
            s += costs[line[j]]
            break
        last = line[j]

    if oldS == s:
        incompleteLines.append(line)

print(s)

scores = []
for line in incompleteLines:
    s = 0
    for j in line[::-1]:
        s *= 5
        match j:
            case "(":
                s += 1
            case "[":
                s += 2
            case "{":
                s += 3
            case "<":
                s += 4
    scores.append(s)

scores.sort()
print(scores[int(len(scores)/2)])
