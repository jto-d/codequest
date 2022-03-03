import sys

# correct

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    lines = int(sys.stdin.readline().rstrip())

    final = []

    for i in range(lines):
        line = sys.stdin.readline().rstrip()

        index = int(line.split('|')[1])
        word = line.split('|')[0]

        final.append(word[index])
    
    print("".join(final))
