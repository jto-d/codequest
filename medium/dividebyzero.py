import sys

cases = int(sys.stdin.readline().rstrip())

def divide(lst):

    try:
        lst[0] = float(lst[0])
    except:
        return 'Invalid Dividend'

    try:
        lst[1] = float(lst[1])
    except:
        return 'Invalid Divisor'

    if int(lst[1]) == 0:
        return 'Divide By Zero'


    div = lst[0]/lst[1]

    # if str(div).split('.')[1]=='0':
    #     return (int(div))
    return div

    
    

for _ in range(cases):
    case = sys.stdin.readline().rstrip().split(' ')
    print(divide(case))
