import sys

cases = int(sys.stdin.readline().rstrip())

class Ship:
    def __init__(self,name,t,x,y):
        self.name = name
        self.type = t
        self.x = int(x)
        self.y = int(y)
        self.move = 0

        if self.type == 'A':
            self.move = 10
        if self.type == 'B':
            self.move = 20
        if self.type == 'C':
            self.move = 30

    def turn(self):
        return self.x - self.move
        

    def __str__(self):
        return str(self.name)

def lowest(ships):
    index = -1
    low = 10000

    if len(ships) == 0:
        return ''

    for i in range(len(ships)):
        if ships[i].turn() < low:
            index = i
    print('Destroyed Ship: ' + str(ships[index]) + ' xLoc: ' + str(ships[index].x))
    ships.pop(index)
    return lowest(ships)


for c in range(cases):
    num = int(sys.stdin.readline().rstrip())
    # key is name
    # value is a list of [type, x coord, y coord]

    ships = []


    for _ in range(num):
        line = sys.stdin.readline().rstrip()

        name = line.split('_')
        typ = name[1].split(':')
        coords = typ[1].split(',')


        ships.append(Ship(name[0],typ[1],coords[0],coords[1]))

    lowest(ships)


    
    




    

