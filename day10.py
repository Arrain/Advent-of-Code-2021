
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
incInput = []
for i in input:
    os = s
    last = i[0]
    i = redPar(i)
    for j in range(1, len(i)):
        if i[j] == ")" and last != "(":
            s += costs.get(i[j])
            break
        if i[j] == "]" and last != "[":
            s += costs.get(i[j])
            break
        if i[j] == "}" and last != "{":
            s += costs.get(i[j])
            break
        if i[j] == ">" and last != "<":
            s += costs.get(i[j])
            break
        last = i[j]

    if os == s:
        incInput.append(i)

print(s)

scores = []
for i in incInput:
    s = 0
    for j in i[::-1]:
        if j == "(":
            s = s * 5 + 1
            continue
        if j == "[":
            s = s * 5 + 2
            continue
        if j == "{":
            s = s * 5 + 3
            continue
        if j == "<":
            s = s * 5 + 4
            continue
    scores.append(s)

scores.sort()
print(scores[int((len(scores)-1)/2)])
