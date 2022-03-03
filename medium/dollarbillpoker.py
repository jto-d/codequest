import sys

# correct

cases = int(sys.stdin.readline().rstrip())

def checkStraight(lst):
    if len(lst) < 5:
        return False
    for i in range(5):
        if (int(lst[i]) - i) != int(lst[0]):
            return checkStraight(lst[1:])
    return True


def check(serial, dic):

    sort = list(dic.values())
    sort.sort()

    vals = list(dic.keys())
    vals.sort()


    if 5 in sort or 6 in sort or 7 in sort or 8 in sort:
        return f'{serial} = FIVE OF A KIND'
    if 4 in sort:
        return f'{serial} = FOUR OF A KIND'
    if sort[-1] == 3 and (sort[-2]==3 or sort[-2]==2):
        return f'{serial} = FULL HOUSE'
    if checkStraight(vals):
        return f'{serial} = STRAIGHT'
    if 3 in sort:
        return f'{serial} = THREE OF A KIND'
    try:
        if sort[-1] == 2 and sort[-2] == 2:
            return f'{serial} = TWO PAIR'
    except:
        if 2 in sort:
            return f'{serial} = PAIR'
        return f'{serial} = {vals[-1]}'
    if 2 in sort:
        return f'{serial} = PAIR'
    return f'{serial} = {vals[-1]}'


    



for _ in range(cases):

    serial = sys.stdin.readline().rstrip()

    num=[]
    for x in serial:
        if x != '0':
            num.append(x)
    
    d = {}
    
    for i in num:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    

    print(check(serial, d))

 
