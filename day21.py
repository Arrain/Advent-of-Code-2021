import math

from numpy import dot, double

input = []

with open("day21_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

playerPos = [8, 4]
playerScore = [0, 0]

diesRolled = 0
dieValue = 1
turn = 0
while playerScore[0] < 1000 and playerScore[1] < 1000:
    move = 0
    for i in range(3):
        move += dieValue
        diesRolled += 1
        dieValue = (dieValue + 1) % 100
        if dieValue == 0:
            dieValue = 100

    playerPos[turn] = (playerPos[turn] + move) % 10
    if playerPos[turn] == 0:
        playerPos[turn] = 10
    playerScore[turn] += playerPos[turn]

    turn = (turn + 1) % 2

print(min(playerScore) * diesRolled)


wei = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

visited = {}


def doTurn(playerScore, playerPos, turn):
    state = (playerScore[0], playerScore[1], playerPos[0], playerPos[1], turn)
    if state in visited:
        return visited[state]

    wins = [0, 0]

    for x in range(3, 10):
        newPlayerPos = playerPos.copy()
        newPlayerScore = playerScore.copy()

        newPlayerPos[turn] = (newPlayerPos[turn] + x) % 10
        if newPlayerPos[turn] == 0:
            newPlayerPos[turn] = 10
        newPlayerScore[turn] += newPlayerPos[turn]

        if newPlayerScore[turn] >= 21:
            wins[turn] += wei[x]
            continue

        val = doTurn(newPlayerScore.copy(), newPlayerPos.copy(), (turn + 1) % 2)
        wins[0] += val[0] * wei[x]
        wins[1] += val[1] * wei[x]

    visited[state] = wins

    return wins


print(max(doTurn([0, 0], [8, 4], 0)))
