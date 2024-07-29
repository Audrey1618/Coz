# https://leetcode.com/discuss/interview-question/4612154/Microsoft-2024-SDE-Intern-OA

def solution(A):
    A = [0] + A + [0]
    res = 0
    for i in range(1, len(A) - 1):
        if A[i - 1] + A[i] + A[i + 1] < 0:
            res += abs(A[i - 1] + A[i] + A[i + 1])
            A[i + 1] += abs(A[i - 1] + A[i] + A[i + 1])
    return res



print("[1, -3, 2]", solution([1, -3, 2])) # 2
print("[-3, 2, 4, -5, 3]", solution([-3, 2, 4, -5, 3])) # 3
print("[-2, 1, -3, 1]", solution([-2, 1, -3, 1])) # 4