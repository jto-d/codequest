import sys

cases = int(sys.stdin.readline().rstrip())

def check(serial, dic):



    if 5 in dic.values():
        return f'{serial} = FIVE OF A KIND'
    if 4 in dic.values():
        return f'{serial} = FOUR OF A KIND'
    if 3 in dic.values() and 2 in dic.values():
        return f'{serial} = FULL HOUSE'
    # straight
    if 3 in dic.values():
        return f'{serial} = THREE OF A KIND'
    


for _ in range(cases):

    serial = sys.stdin.readline().rstrip()

    num=[]
    for x in serial:
        if x != '0':
            num.append(x)
    print(num)
    
    d = {}
    
    for i in num:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    

    print(check(serial, d))

 
