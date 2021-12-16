import math

input = []

with open("day16_input.txt") as file:
    input = [line.strip() for line in file.readlines()]

toBit = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

newInput = ""
for i in input[0]:
    newInput += toBit[i]

vc = 0

print(newInput)

def parsePacket(code):
    global vc
    global expr

    vvv = int(code[:3], 2)
    code = code[3:]
    vc += vvv

    ttt = int(code[:3], 2)
    code = code[3:]

    if ttt == 4:
        rep = ""
        while True:
            cont = code[0]

            rep += code[1:5]
            code = code[5:]

            if cont != "1":
                break
        rep = int(rep, 2)
        return (code, rep)
    else:
        sp = []
        if code[0] == "0":
            l = int(code[1:16], 2)
            code = code[16:]
            nc = code[:l]
            while True:
                nsp = parsePacket(nc)
                sp.append(nsp)
                nc = nsp[0]
                if len(nc) == 0:
                    break
            code = code[l:]
        else:
            l = int(code[1:12], 2)
            code = code[12:]
            for i in range(l):
                nsp = parsePacket(code)
                sp.append(nsp)
                code = nsp[0]

        match ttt:
            case 0:
                return (code, sum(x[1] for x in sp))
            case 1:
                return (code, math.prod(x[1] for x in sp))
            case 2:
                return (code, min(x[1] for x in sp))
            case 3:
                return (code, max(x[1] for x in sp))
            case 5:
                return (code, 1 if sp[0][1] > sp[1][1] else 0)
            case 6:
                return (code, 1 if sp[0][1] < sp[1][1] else 0)
            case 7:
                return (code, 1 if sp[0][1] == sp[1][1] else 0)


print(parsePacket(newInput))
print(vc)