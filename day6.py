
input = []

with open("day6_input.txt") as file:
    input = [list(map(lambda i: int(i), line.split(",")))
             for line in file.readlines()]

fish = input[0]
for i in range(80):
    print(i, len(fish))
    newFish = []
    for f in range(len(fish)):
        if(fish[f] == 0):
            newFish.append(8)
            fish[f] = 6
        else:
            fish[f] -= 1

    fish.extend(newFish)

print(len(fish))

gFish = list(map(lambda x: 0, range(9)))
for i in input[0]:
    gFish[i] += 1
for i in range(257):
    # print(gFish)
    newFish = gFish[0]
    for f in range(1, 9):
        gFish[f-1] = gFish[f]
    gFish[6] += newFish
    gFish[8] = newFish
    print(i, sum(gFish))
