from sys import dont_write_bytecode


data = list(map(lambda x : list(map(lambda y: len(y), x.split(" | ")[1].split(" "))), open("day8.txt", "r").read().splitlines()))

data1 = list(map(lambda x : list(map(lambda y: set(y), x.split(" | ")[1].split(" "))), open("day8.txt", "r").read().splitlines()))

data2 =  list(map(lambda x : list(map(lambda y: set(y), x.split(" | ")[0].split(" "))), open("day8.txt", "r").read().splitlines()))


def findKnown(digits):
    known = {"size5":[],"size6":[]}
    for i in digits:
        if len(i) == 2:
            known[1] = i
        elif len(i) == 4:
            known[4] = i
        elif len(i) == 3:
            known[7] = i
        elif len(i) == 7:
            known[8] = i
        elif len(i) == 5:
            known["size5"].append(i)
        elif len(i) == 6:
            known["size6"].append(i)
    return known


def translator(digits):
    k = findKnown(digits)
    for i in k["size6"]:
        if (len(k[7].union(k[4]).difference(i)) == 0):
            k[9] = i
            k["size6"].remove(i)

    for i in k["size5"]:
        if len(k[9].union(i)) == 7:

            k[2] = i
            k["size5"].remove(i)
    
    l = k[4].difference(k[1])
    

    top = k[7].difference(k[1])
    middle = k[2].difference(k[1]).intersection(k[4])
    topLeft = l.difference(middle)
    k[0] = k[8].difference(middle)
    k["size6"].remove(k[0])
    k[6] = k["size6"][0]
    k["size6"].remove(k[6])

    bottomLeft = k[0].difference(k[9])
    bottom = k[2].difference(k[1],top,middle, bottomLeft)
    k[3] = k[4].union(bottom,top).difference(topLeft)
    k["size5"].remove(k[3])
    k[5] = k["size5"].pop()

    return k


def solve1(data):
    cnt = 0
    for i in data:
        cnt += i.count(2)
        cnt += i.count(7)
        cnt += i.count(3)
        cnt += i.count(4)
    return cnt

def solve2(data1,data2):
    numbers = []
    
    for note, tr in zip(data1, data2):
        number =""
        for i in note:
            for k,v in translator(tr).items():
                if v == i:
                    number += str(k)
        numbers.append(int(number))
    return sum(numbers)

print("day8 part1 :", solve1(data))
print("day8 part2 :", solve2(data1,data2))
print("-"*25)