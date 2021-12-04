
input = []

with open("day4_input.txt") as file:
    input = [line for line in file.readlines()]


def checkBoard(board, val):
    for i in range(5):
        for j in range(5):
            if board[i][j][0] == val:
                board[i][j][1] = True

    for i in range(5):
        q = True
        for j in range(5):
            if board[i][j][1] == False:
                q = False
                break
        if q:
            return True

        q = True
        for j in range(5):
            if board[j][i][1] == False:
                q = False
                break
        if q:
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

for i in range(2, len(input)-1, 6):
    board = []
    for j in range(5):
        line = list(map(lambda x: [int(x), False], input[i+j].split()))
        board.append(line)
    boards.append([board, False])

# for i in draws:
#     for b in boards:
#         if b[1]:
#             continue
#         r = checkBoard(b[0], i)
#         if r:
#             print(processBoard(b[0], i))
#             exit()

last = 0

for i in draws:
    for b in boards:
        if b[1]:
            continue
        r = checkBoard(b[0], i)
        if r:
            last = processBoard(b[0], i)
            b[1] = True
print(last)
