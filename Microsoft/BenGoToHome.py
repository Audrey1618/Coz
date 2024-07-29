# https://leetcode.com/discuss/interview-question/4766971/Microsoft-OA-or-3-Questions-or-75-Minutes

def solution(A, B):
    res = 0

    for i in range(len(B)):
        res += A[i]
        if B[i] % 120 == 0:
            continue
        else:
            res += B[i]
    
    res += A[-1]

    return res


print("[240, 800, 100], [60, 120]", solution([240, 800, 100], [60, 120])) # 1200

