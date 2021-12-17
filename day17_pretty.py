from util import Coord2D

input = []

with open("day17_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

targMin = Coord2D(70, -159)
targMax = Coord2D(125, -121)


def doStep(pos: Coord2D, vel: Coord2D):
    pos.x += vel.x
    pos.y += vel.y

    if vel.x > 0:
        vel.x -= 1
    elif vel.x < 0:
        vel.x += 1

    vel.y -= 1


def doLaunch(pos: Coord2D, vel: Coord2D):
    steps = 0
    yMax = pos.y
    while True:
        doStep(pos, vel)

        if pos.y > yMax:
            yMax = pos.y

        if targMin.x <= pos.x <= targMax.x and targMin.y <= pos.y <= targMax.y:
            return (True, steps, yMax)

        if pos.y < targMin.y:
            return (False, steps, yMax)

        steps += 1


pos = Coord2D()
vel = Coord2D(15, 158)
print(doLaunch(pos, vel))

cnt = 0
for x in range(targMax.x + 1):
    for y in range(targMin.y - 1, -(targMin.y) + 1):
        rez = doLaunch(Coord2D(), Coord2D(x, y))
        if rez[0]:
            cnt += 1
print(cnt)
