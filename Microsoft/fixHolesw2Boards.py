# https://leetcode.com/discuss/interview-question/4944166/Microsoft-Software-Engineer-I-OA

def solution(A):
    A.sort()
    # print(A)
    def canFix(A, m):
        if A[m] - A[0] >= A[-1] - A[m + 1]:
            return True
        else:
            return False
    l, r = 0, len(A) - 1
    mark = -1
    while l <= r:
        m = (l + r) // 2
        if canFix(A, m):
            mark = m
            r = m - 1
        else:
            l = m + 1

    return min(A[mark] - A[0], A[-1] - A[mark])
        

print("[11, 20, 15]", solution([11, 20, 15]))
# res = 4

print("[15, 20, 9, 11]", solution([15, 20, 9, 11]))
# res = 5

print("[0, 44, 32, 30, 42, 18, 34, 16, 35]", solution([0, 44, 32, 30, 42, 18, 34, 16, 35]))
# res = 18
