data = list(map(lambda x : int(x), open("day6.txt", "r").read().split(",")))




initial = {"eight": data.count(8), "seven": data.count(7), "six" : data.count(6), "five":data.count(5), "four": data.count(4), "three": data.count(3), "two":data.count(2), "one":data.count(1), "zero": data.count(0)}


def round(initial :dict):
    newData = {}

    newData["seven"] = initial["eight"]
    newData["six"] = initial["seven"]
    newData["five"] = initial["six"]
    newData["four"] = initial["five"]
    newData["three"] = initial["four"]
    newData["two"] = initial["three"]
    newData["one"] = initial["two"]
    newData["zero"] = initial["one"]
    newData["eight"] = initial["zero"]
    newData["six"] += initial["zero"]
    return newData


def solve1(initial):
    for i in range(0,80):
        initial = round(initial)
    return sum(initial.values())

def solve2(initial):
    for i in range(0,256):
        initial = round(initial)
    return sum(initial.values())


print("day6 part1 :", solve1(initial))
print("day6 part2 :", solve2(initial))
print("-"*25)