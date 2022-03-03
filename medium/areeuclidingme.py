import sys

# correct

cases = int(sys.stdin.readline().rstrip())

def euclid(x, y):
    if x > y:
        m = x
        s = y
    else:
        m = y
        s = x

    
    d = m - s

    if d == 0 and s == 1:
        print(str(m) + '-' + str(s) + '=' + str(d))
        return 'COPRIME'
    elif d == 0:
        print(str(m) + '-' + str(s) + '=' + str(d))
        return 'NOT COPRIME'
    else:
        print(str(m) + '-' + str(s) + '=' + str(d))
        return euclid(s,d)


for _ in range(cases):
    nums = sys.stdin.readline().rstrip()

    x = int(nums.split(',')[0])
    y = int(nums.split(',')[1])

    print(euclid(x, y))


    

