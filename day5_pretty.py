
input = []

with open("day5_input.txt") as file:
    input = [line for line in file.readlines()]

vents = []
for i in input:
    tmp = list(map(lambda j:
                   list(map(lambda k: int(k), j.split(","))), i.split(" -> ")))
    vents.append([tmp[0], tmp[1]])


dmgMap = dict()


def addToDmgMap(key):
    if key in dmgMap:
        dmgMap[key] += 1
    else:
        dmgMap[key] = 1


for v in vents:
    if v[0][0] == v[1][0]:
        for q in range(min(v[0][1], v[1][1]),
                       max(v[0][1], v[1][1]) + 1):
            addToDmgMap(f"{v[0][0]},{q}")

    if v[0][1] == v[1][1]:
        for q in range(min(v[0][0], v[1][0]),
                       max(v[0][0], v[1][0]) + 1):
            addToDmgMap(f"{q},{v[0][1]}")


print(sum(map(lambda v: v > 1, dmgMap.values())))

dmgMap = dict()
for v in vents:
    if v[0][0] == v[1][0]:
        for q in range(min(v[0][1], v[1][1]),
                       max(v[0][1], v[1][1]) + 1):
            addToDmgMap(f"{v[0][0]},{q}")

    if v[0][1] == v[1][1]:
        for q in range(min(v[0][0], v[1][0]),
                       max(v[0][0], v[1][0]) + 1):
            addToDmgMap(f"{q},{v[0][1]}")

    if abs(v[0][0] - v[1][0]) == abs(v[0][1] - v[1][1]):
        x = v[0][0]
        y = v[0][1]

        for q in range(-1, abs(v[0][0] - v[1][0])):
            addToDmgMap(f"{x},{y}")

            x += 1 if v[0][0] < v[1][0] else -1
            y += 1 if v[0][1] < v[1][1] else -1

print(sum(map(lambda v: v > 1, dmgMap.values())))
