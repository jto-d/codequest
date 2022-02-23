import sys
import math
import string



cases = int(sys.stdin.readline().rstrip())


for c in range(cases):
    case = int(sys.stdin.readline().rstrip())
    nums = []
    for _ in range(case):
        nums.append(int(sys.stdin.readline().rstrip()))

    print(str(sum(nums)))
