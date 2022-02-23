import sys
import math
import string


files_len = int(sys.stdin.readline().rstrip())
dic = {}

for _ in range(files_len):
    end = sys.stdin.readline().rstrip().split('.')[1]
    if end in dic.keys():
        dic[end] += 1
    else:
        dic[end] = 1
fin = ''
for key in dic.keys():
    fin += (key + ' ' + str(dic[key]) + '\n')
print(fin.rstrip())

        
