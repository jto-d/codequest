import sys

cases = int(sys.stdin.readline().rstrip())

def func(num: str, ite: int, lst: list):
    
    split = num.split('.')
    right = split[1]

    if ite == 9:
        lst.append(str(split[0]))
        return lst

    lst.append(split[0])

    value = 1/float('.' + right)    
    ite += 1

    return func(str(value), ite, lst)

for _ in range(cases):
    case = sys.stdin.readline().rstrip()

    print(func(case, 0, []))


