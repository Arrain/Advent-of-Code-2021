
input = []

with open("day5_input.txt") as file:
    input = [line for line in file.readlines()]

vents = []
for i in input:
    tmp = list(map(lambda x:
                   list(map(lambda y: int(y), x.split(","))), i.split(" -> ")))
    vents.append([tmp[0], tmp[1]])

dmgMap = dict()
for v in vents:
    if v[0][0] == v[1][0]:
        for q in range(min(v[0][1], v[1][1]), max(v[0][1], v[1][1])+1):
            k = str(v[0][0]) + "," + str(q)
            if k in dmgMap:
                dmgMap[k] += 1
            else:
                dmgMap[k] = 1
    if v[0][1] == v[1][1]:
        for q in range(min(v[0][0], v[1][0]), max(v[0][0], v[1][0])+1):
            k = str(q) + "," + str(v[0][1])
            if k in dmgMap:
                dmgMap[k] += 1
            else:
                dmgMap[k] = 1

c = 0
for d in dmgMap.values():
    if d > 1:
        c += 1

print(c)

dmgMap = dict()
for v in vents:
    if v[0][0] == v[1][0]:
        for q in range(min(v[0][1], v[1][1]), max(v[0][1], v[1][1])+1):
            k = str(v[0][0]) + "," + str(q)
            if k in dmgMap:
                dmgMap[k] += 1
            else:
                dmgMap[k] = 1
    if v[0][1] == v[1][1]:
        for q in range(min(v[0][0], v[1][0]), max(v[0][0], v[1][0])+1):
            k = str(q) + "," + str(v[0][1])
            if k in dmgMap:
                dmgMap[k] += 1
            else:
                dmgMap[k] = 1

    if abs(v[0][0] - v[1][0]) == abs(v[0][1] - v[1][1]):
        dif = abs(v[0][0] - v[1][0])
        x = v[0][0]
        y = v[0][1]
        k = str(x) + "," + str(y)
        if k in dmgMap:
            dmgMap[k] += 1
        else:
            dmgMap[k] = 1
        for q in range(dif):
            if v[0][0] < v[1][0]:
                x += 1
            else:
                x -= 1
            if v[0][1] < v[1][1]:
                y += 1
            else:
                y -= 1

            k = str(x) + "," + str(y)
            if k in dmgMap:
                dmgMap[k] += 1
            else:
                dmgMap[k] = 1

c = 0
for d in dmgMap.values():
    if d > 1:
        c += 1

print(c)
