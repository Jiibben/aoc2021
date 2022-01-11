import math
data = list(map(lambda x : int(x),open("day7.txt", "r").read().split(",")))
borneInf = min(data)
borneSup = max(data)

def calculateNeed1(data, point):
    counter = 0
    for i in data:
        difference = abs(i -point)
        counter += difference
    return counter


def calculateNeed2(data, point):
    counter = 0
    for i in data:
        difference = abs(i -point)
        counter += (difference * (difference+1)) /2
    return counter

def solve1(data):
    fuelNeed = []
    for i in range(borneInf, borneSup+1):
        fuelNeed.append(calculateNeed1(data, i))
    
    return min(fuelNeed)

def solve2(data):
    fuelNeed = []
    for i in range(borneInf, borneSup+1):
        fuelNeed.append(calculateNeed2(data, i))
    
    return min(fuelNeed)


print("day7 part1 : ", solve1(data))

print("day7 part2 : ", solve2(data))
print("-"*25)