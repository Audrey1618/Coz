def solution(A):
    res = 0
    exist = {}
    prevSum = -1
    for i in range(len(A) - 1):
        currSum = A[i] + A[i + 1]
        if currSum not in exist:
            exist[currSum] = 1
            prevSum = currSum
        elif currSum != prevSum:
            exist[currSum] += 1
            prevSum = currSum
        else:
            prevSum = -1
        res = max(res, exist[currSum])
    return res


print(solution([10, 1, 3, 1, 2, 2, 1, 0, 4]))