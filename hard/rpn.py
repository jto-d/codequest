from inspect import stack
import sys

case = sys.stdin.readline().rstrip()

case = case.split(' ')
print(case)

def rpn_trip(ex):
    index = 1
    lst = [item for item in ex]
    lst[index] = ex[index+1]
    lst[index+1] = ex[index]
    return lst

case.insert(0, rpn_trip([case.pop(0),case.pop(0),case.pop(0)]))

print(case)

print(rpn_trip(case))


