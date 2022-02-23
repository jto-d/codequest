import sys

cases = int(sys.stdin.readline().rstrip())

vowels = ['a', 'e', 'i', 'o', 'u']

for line in range(cases):
    c = 0
    line = sys.stdin.readline().rstrip()
    for let in line:
        if let in vowels:
            c+=1
    print(c)

