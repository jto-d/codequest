import sys


cases = int(sys.stdin.readline().rstrip())

def solve(msg, shifts, d):
    nums = [ord(let) for let in msg]
    s_len = len(shifts)
    d_len = len(d)

    sub = 0

    for i in range(len(nums)):
        mult = 1
        if nums[i] >= 97 and nums[i] <= 122:
            if d[(i-sub)%d_len] == 1:
                mult = -1
                if nums[i] + mult * shifts[(i-sub)%s_len] < 97:
                    nums[i] = 122 + nums[i] - 97
            else:
                if nums[i] + mult * shifts[(i-sub)%s_len] > 122:
                    nums[i] = 96 - (122 - nums[i])

            nums[i] += mult * shifts[(i-sub)%s_len]
        else:
            sub+=1
        
    
    lets = ''.join([chr(let) for let in nums])
    
    print(lets)

        

for c in range(cases):

    msg = sys.stdin.readline().rstrip().lower()
    shifts = sys.stdin.readline().rstrip().split(' ')
    d = sys.stdin.readline().rstrip().split(' ')
    
    shifts = [int(item) for item in shifts]
    d = [int(item) for item in d]

    solve(msg,shifts,d)
    
    