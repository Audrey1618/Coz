# https://leetcode.com/discuss/interview-question/4471415/Microsoft-OA

from collections import defaultdict
def solution(A):
    res = 0
    A.sort()
    print(A)
    r = 0
    exist = defaultdict(list)
    for i in range(len(A) - 1):
        j = 1
        while i + j < len(A):
            gap = A[i + j] - A[i]
            if len(exist[gap]) ==  0 or (len(exist[gap]) > 0 and exist[gap][-1][1] <= A[i]):
                exist[gap].append([A[i], A[i + j]])
            j += 1
    return res
    
    # for i in range()
    print(exist)
    
   
print('[4, 7, 1, 5, 3] || res =', solution([4, 7, 1, 5, 3])) # res = 4

print('[12, 12, 12, 15, 10] || res =', solution([12, 12, 12, 15, 10])) # res = 3

print('[18, 26, 18, 24, 24, 20, 22] || res =', solution([18, 26, 18, 24, 24, 20, 22])) # res = 5
