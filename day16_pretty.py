import math

input = []

with open("day16_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

newInput = "".join(format(int(i, 16), "04b") for i in input[0])

versSum = 0

def parsePacket(code):
    global versSum

    vers = int(code[:3], 2)
    versSum += vers
    code = code[3:]

    typeId = int(code[:3], 2)
    code = code[3:]

    if typeId == 4:
        literalValue = ""
        while True:
            cont = code[0]

            literalValue += code[1:5]
            code = code[5:]

            if cont != "1":
                break
            
        return (code, int(literalValue, 2))
    else:
        subPacks = []
        
        if code[0] == "0":
            l = int(code[1:16], 2)
            code = code[16:]
            auxCode = code[:l]
            while True:
                newSubPack = parsePacket(auxCode)
                subPacks.append(newSubPack)
                auxCode = newSubPack[0]
                if len(auxCode) == 0:
                    break
            code = code[l:]
        else:
            l = int(code[1:12], 2)
            code = code[12:]
            for i in range(l):
                newSubPack = parsePacket(code)
                subPacks.append(newSubPack)
                code = newSubPack[0]

        match typeId:
            case 0:
                return (code, sum(x[1] for x in subPacks))
            case 1:
                return (code, math.prod(x[1] for x in subPacks))
            case 2:
                return (code, min(x[1] for x in subPacks))
            case 3:
                return (code, max(x[1] for x in subPacks))
            case 5:
                return (code, 1 if subPacks[0][1] > subPacks[1][1] else 0)
            case 6:
                return (code, 1 if subPacks[0][1] < subPacks[1][1] else 0)
            case 7:
                return (code, 1 if subPacks[0][1] == subPacks[1][1] else 0)


print(parsePacket(newInput))
print(versSum)
