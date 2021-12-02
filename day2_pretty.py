
input = []

with open("day2_input.txt") as file:
    input = [line.split(" ") for line in file.readlines()]

horz = 0
vert = 0
for i in input:
    c = int(i[1])
    if i[0][0] == "f":
        horz += c
    elif i[0][0] == "d":
        vert += c
    else:
        vert -= c
print(horz * vert)

horz = 0
vert = 0
aim = 0
for i in input:
    c = int(i[1])
    if i[0][0] == "f":
        horz += c
        vert += aim * c
    elif i[0][0] == "d":
        aim += c
    else:
        aim -= c
print(horz * vert)
