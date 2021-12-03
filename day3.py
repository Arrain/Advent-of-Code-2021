
input = []

with open("day3_input.txt") as file:
    input = [line for line in file.readlines()]

c = 0
lim = len(input[0])
print(lim)
g = ""
e = ""
for l in range(lim-1):
    f0 = 0
    f1 = 0
    for i in input:
        if i[l] == "1":
            f1 += 1
        else:
            f0 += 1
    if f0 > f1:
        g += "0"
        e += "1"
    else:
        g += "1"
        e += "0"

print(int(g, 2))
print(int(e, 2))
print(int(e, 2)*int(g, 2))
print("*********")

prox = input.copy()

while(len(prox) > 1):
    for l in range(lim-1):
        f0 = 0
        f1 = 0
        q = "1"
        for i in prox:
            if i[l] == "1":
                f1 += 1
            else:
                f0 += 1
        if f0 > f1:
            q = "0"

        mat = []
        for i in prox:
            if i[l] == q:
                mat.append(i)
        prox = mat

a = int(prox[0], 2)
print(a)

prox = input.copy()

while(len(prox) > 1):
    for l in range(lim-1):
        f0 = 0
        f1 = 0
        for i in prox:
            if i[l] == "1":
                f1 += 1
            else:
                f0 += 1
        q = "0"
        if f1 < f0:
            q = "1"
        mat = []
        print(q)
        for i in prox:
            if i[l] == q:
                mat.append(i)
        prox = mat

        if(len(prox) == 1):
            break  # sigh


b = int(prox[0], 2)
print(a, b, a*b)
