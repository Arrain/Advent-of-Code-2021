input = []

with open("day17_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

targXmin = 70
targXmax = 125
targYmin = -159
targYmax = -121


class Coord:
    x = 0
    y = 0


def doStep(pos, vel):
    pos.x += vel.x
    pos.y += vel.y
    if vel.x > 0:
        vel.x -= 1
    elif vel.x < 0:
        vel.x += 1

    vel.y -= 1

    return (pos, vel)


def doLaunch(pos, vel):
    c = 0
    yMax = pos.y
    while True:
        rez = doStep(pos, vel)
        pos = rez[0]
        vel = rez[1]
        if pos.y > yMax:
            yMax = pos.y
        if targXmin <= pos.x <= targXmax and targYmin <= pos.y <= targYmax:
            return (True, c, yMax)
        if pos.y < targYmin:
            return (False, c, yMax)
        c += 1


pos = Coord()
vel = Coord()
vel.x = 14
vel.y = 158

print(doLaunch(pos, vel))

cnt = 0
for x in range(targXmax + 1):
    for y in range(targYmin - 1, -targYmin + 1):
        pos = Coord()
        vel = Coord()
        vel.x = x
        vel.y = y
        rez = doLaunch(pos, vel)
        if rez[0]:
            cnt += 1
print(cnt)
