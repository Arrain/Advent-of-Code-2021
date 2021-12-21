input = []

with open("day21_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

playerPos = [8, 4]
playerScore = [0, 0]

diesRolled = 0
dieValue = 1
turn = 0
while max(playerScore) < 1000:
    move = 0
    for i in range(3):
        move += dieValue
        diesRolled += 1
        dieValue = dieValue % 100 + 1

    playerPos[turn] = (playerPos[turn] + move - 1) % 10 + 1
    playerScore[turn] += playerPos[turn]

    turn = (turn + 1) % 2

print(min(playerScore) * diesRolled)


chances = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

states = {}


def doTurn(playerScore, playerPos, turn):
    currentState = (*playerScore, *playerPos, turn)
    if currentState in states:
        return states[currentState]

    wins = [0, 0]

    for x in chances.keys():
        newPlayerPos = playerPos.copy()
        newPlayerScore = playerScore.copy()

        newPlayerPos[turn] = (newPlayerPos[turn] + x - 1) % 10 + 1
        newPlayerScore[turn] += newPlayerPos[turn]

        if newPlayerScore[turn] >= 21:
            wins[turn] += chances[x]
            continue

        rez = doTurn(newPlayerScore, newPlayerPos, (turn + 1) % 2)
        wins[0] += rez[0] * chances[x]
        wins[1] += rez[1] * chances[x]

    states[currentState] = wins

    return wins


print(max(doTurn([0, 0], [8, 4], 0)))
