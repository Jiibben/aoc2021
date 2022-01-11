


data = list(map(lambda x: list(map( lambda x : tuple(map(lambda x: int(x), x.split(","))), x.split(" -> "))) ,open("day5.txt", "r").read().splitlines()))

class Line:
    def __init__(self, startingPoint : tuple, endingPoint : tuple):
        self.startingPoint = Point(startingPoint[0], startingPoint[1])
        self.endingPoint = Point(endingPoint[0], endingPoint[1])



    
    def slope(self):
        try:
            slope = (self.endingPoint.y -self.startingPoint.y) / (self.endingPoint.x -self.startingPoint.x)
        except ZeroDivisionError:
            slope = 0
        return slope

    def coveringPoints(self):
        covering = set()
        spX = self.startingPoint.x
        spY = self.startingPoint.y
        epX = self.endingPoint.x
        epY = self.endingPoint.y
        covering.add((epX, epY))
        covering.add((spX, spY))
        while True:
            covering.add((epX, epY))


            if spX < epX:
                epX-=1
            elif spX > epX:
                epX+=1
            
            if spY < epY:
                epY-=1
            elif spY > epY:
                epY+=1

            

            if epX== spX and epY == spY:  
                covering.add((spX, spY)) 
                return covering

    def coveringStraight(self):
        covering = set()
        spX = self.startingPoint.x
        spY = self.startingPoint.y
        epX = self.endingPoint.x
        epY = self.endingPoint.y
       
        if self.slope() == 0.0:
            covering.add((epX, epY))
            covering.add((spX, spY))
            while True:
                covering.add((epX, epY))


                if spX < epX:
                    epX-=1
                elif spX > epX:
                    epX+=1
                
                if spY < epY:
                    epY-=1
                elif spY > epY:
                    epY+=1

                
                if epX== spX and epY == spY:  
                    covering.add((spX, spY)) 
                    return covering
        return covering
class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y

    
def solve1(data):
    counter = {}
    for i in data:
        li = Line(i[0], i[1])
        for d in li.coveringStraight():
            if d in counter.keys():
                counter[d] = 2
            else:
                counter[d] = 0
    return len(list(filter(lambda d : d>1, counter.values())))

def solve2(data):
    counter = {}
    for i in data:
        li = Line(i[0], i[1])
        for d in li.coveringPoints():
            if d in counter.keys():
                counter[d] = 2
            else:
                counter[d] = 0
    return len(list(filter(lambda d : d>1, counter.values())))
        
print("day5 part1 :", solve1(data))

print("day5 part2 :", solve2(data))
print("-"*25)