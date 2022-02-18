import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    line = sys.stdin.readline().rstrip().split(' ')
    out = ''
    for i in range(len(line)):
        if line[i] == 'M':
            out += str(i + 1) + ' '
    print(out[:-1])
