# https://leetcode.com/discuss/interview-question/4944166/Microsoft-Software-Engineer-I-OA
from collections import defaultdict
def solution(A):
    remain = sum(A)
    cus = {}
    line = []
    
    for i in range(len(A)):
        cus[i + 1] = A[i]
    
    i = 1
    while remain > 0:
        if cus[i] != 0:
            cus[i] -= 1
            remain -= 1
            line.append(i)
            # print(line)
        i += 1

        if i == len(A) + 1:
            i = 1
    
    # print(line)
    exist = defaultdict(int)
    # print(line)
    for i in range(len(line)):
        exist[line[i]] = i

    # print(exist)
    return sum(exist.values()) + len(exist.keys())
 

print("[3, 1, 2] result =", solution([3, 1, 2])) # 13
print("[1, 2, 3, 4] result =", solution([1, 2, 3, 4])) # 24
print("[7, 7, 7] result =", solution([7, 7, 7])) # 60



