
input = []

with open("day4_input.txt") as file:
    input = [line.strip() for line in file.readlines()]


def checkBoard(board, val):
    for i in range(5):
        for j in range(5):
            if board[i][j][0] == val:
                board[i][j][1] = True

    for i in range(5):
        if all(board[i][j][1] == True for j in range(5)):
            return True

        if all(board[j][i][1] == True for j in range(5)):
            return True

    return False


def processBoard(board, val):
    s = 0
    for i in range(5):
        for j in range(5):
            if board[i][j][1] == False:
                s += board[i][j][0]
    return s * val


draws = list(map(lambda x: int(x), input[0].split(",")))

boards = []

for i in range(2, len(input), 6):
    board = []
    for j in range(5):
        board.append(
            list(map(lambda x: [int(x), False], input[i+j].split()))
        )
    boards.append([board, False])


firstFound = False
last = 0
for i in draws:
    for b in boards:
        if b[1]:
            continue
        if checkBoard(b[0], i):
            last = processBoard(b[0], i)
            b[1] = True
            if not firstFound:
                print(last)
                firstFound = True

print(last)
