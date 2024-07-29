A = [-4,2,3,4,5]

A.sort()

print(A)

def solution(nums):
    ans = 1 # gan ans = 1

    for n in nums:
        if n == ans: # neu gap 1 cai ko phai ans thi day ans len 1
            ans += 1
    return ans
 
print(solution(A))