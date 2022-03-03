import sys

cases = int(sys.stdin.readline().rstrip())

def toBinary(num, bound, bi, chars):
    if num==0:
        while(len(bi)<chars):
            bi += '0'
        return bi

      
    if num < 2**(bound-1):
        bi += '0'
    else:
        bi += '1'
        num -= 2**(bound-1)
    
    return toBinary(num,bound-1,bi,chars)
    
# for i in range(2**(3)):
#     print(toBinary(i,3,''))


for _ in range(cases):
    b = int(sys.stdin.readline().rstrip())

    

    for i in range(2**b):
        print(toBinary(i,b,'',b))
