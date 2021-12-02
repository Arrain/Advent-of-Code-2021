
input = []

with open("day2_input.txt") as f:
    input = [l.split(" ") for l in f.readlines()]

h = 0
v = 0
for i in input:
    if i[0][0] == "f":
        h += int(i[1])
    elif i[0][0] == "d":
        v += int(i[1])
    else:
        v -= int(i[1])
print(h * v)

h = 0
a = 0
v = 0
for i in input:
    if i[0][0] == "f":
        h += int(i[1])
        v += a * int(i[1])
    elif i[0][0] == "d":
        a += int(i[1])
    else:
        a -= int(i[1])
print(h * v)
