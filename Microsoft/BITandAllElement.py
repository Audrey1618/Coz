# https://leetcode.com/discuss/interview-question/3781043/hackerrank-oa/
from collections import defaultdict
def solution(A):
    c = [0] * 31
    for x in A:
        for j in range(0, 31):
            if x == 0:
                break
            c[j] += x & 1 # xem bit ngoai cung hien tai cua x co phai la 1 hay ko? neu la 1 thi count la tai vi tri j xuat hien so 1. 
            
            x >>= 1 # dich bit de tiep tuc so sanh xem no co phai 1 hay ko
    return max(c)
    
    #-------------------------------------------
    # def convert(i):
    #     return str(bin(i+2**32)[-32:])

    # exist = defaultdict(int)
    # for x in A:
    #     x = convert(x)
    #     for j in range(0, 32):
    #         if x[j] == '1':
    #             exist[j] = exist.get(j, 0) + 1
    #     # print(exist)
    # return max(exist.values())

print(solution([13, 7, 2, 8, 3])) # res = 3
print(solution([1, 2, 4, 8])) # res = 1
print(solution([16, 16])) # res = 2