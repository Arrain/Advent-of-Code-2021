import math

input = []

with open("day18_input.txt") as file:
    input = [line.strip() for line in file.readlines()]


digits = [str(i) for i in range(10)]


def findExplosion(snail):
    cnt = 0
    for i in range(len(snail)):
        if snail[i] == "[":
            cnt += 1
        if snail[i] == "]":
            cnt -= 1

        if cnt > 4:
            for j in range(i + 1, len(snail)):
                if snail[j] == "[":
                    break
                elif snail[j] == "]":
                    return i

    return -1


def findSplit(snail):
    for i in range(len(snail) - 1):
        if snail[i] in digits and snail[i + 1] in digits:
            return i

    return -1


def doExplosion(snail, indExpStart):
    exp = snail[indExpStart + 1 :].partition("]")[0]
    expParts = exp.split(",")
    expLeft = int(expParts[0])
    expRight = int(expParts[1])

    indExpEnd = indExpStart + 1 + len(exp) + 1

    leftSide = snail[:indExpStart]

    for i in reversed(range(indExpStart)):
        if snail[i] in digits:
            leftNum = ""
            j = i
            while snail[j] in digits:
                leftNum += snail[j]
                j -= 1
            leftNum = int(leftNum[::-1]) + expLeft

            leftSide = snail[: j + 1] + str(leftNum) + snail[i + 1 : indExpStart]
            break

    rightSide = snail[indExpEnd:]

    for i in range(indExpEnd, len(snail)):
        if snail[i] in digits:
            rightNum = ""
            j = i
            while snail[j] in digits:
                rightNum += snail[j]
                j += 1
            rightNum = int(rightNum) + expRight

            rightSide = snail[indExpEnd:i] + str(rightNum) + snail[j:]
            break

    return leftSide + "0" + rightSide


def doSplit(snail, ind):
    num = ""
    j = ind
    while snail[j] in digits:
        num += snail[j]
        j += 1
    num = int(num)
    return f"{snail[:ind]}[{math.floor(num/2)},{math.ceil(num/2)}]{snail[j:]}"


def reduceSnail(snail):
    while True:
        explosionIndex = findExplosion(snail)
        if explosionIndex >= 0:
            snail = doExplosion(snail, explosionIndex)
            continue

        splitIndex = findSplit(snail)
        if splitIndex >= 0:
            snail = doSplit(snail, splitIndex)
            continue

        return snail


def calcMagnitude(snail):
    snailChanged = True
    while snailChanged:
        snailChanged = False
        for i in range(len(snail)):
            if snail[i] == "[":
                for j in range(i + 1, len(snail)):
                    if snail[j] == "[":
                        break
                    if snail[j] == "]":
                        parts = snail[i + 1 : j].split(",")
                        val = int(parts[0]) * 3 + int(parts[1]) * 2
                        snail = snail[:i] + str(val) + snail[j + 1 :]
                        snailChanged = True
                        break
                if snailChanged:
                    break
    return snail


finalSnail = input[0]
for i in range(1, len(input)):
    newSnail = f"[{finalSnail},{input[i]}]"
    finalSnail = reduceSnail(newSnail)

print(calcMagnitude(finalSnail))


maxMagnitude = 0

for i in range(len(input) - 1):
    for j in range(i + 1, len(input)):
        mag = int(calcMagnitude(reduceSnail(f"[{input[i]},{input[j]}]")))
        if mag > maxMagnitude:
            maxMagnitude = mag
        mag = int(calcMagnitude(reduceSnail(f"[{input[j]},{input[i]}]")))
        if mag > maxMagnitude:
            maxMagnitude = mag

print(maxMagnitude)
