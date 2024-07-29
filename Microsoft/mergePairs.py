# https://leetcode.com/discuss/interview-question/4986072/Microsoft-or-OA-or-Maximum-Sum-of-Merged-Array-Pairs
def solution(a):
    n = len(a)
    dp = [0] * (n + 1)     # dp[n] is 0
    dp[n - 1] = a[n - 1]   # base case
    print(dp)
    print(a)
    for i in range(n - 2, -1, -1):
        # neu ko ghep thi kq ghep hien tai = a[i] + dp[i + 1]
        notMakePair = a[i] + dp[i + 1] 
        # neu chon ghep thi kq ghep hien tai = ghep a[i]a[i + 1] + dp[i + 2]
        makePair = int(str(a[i]) + str(a[i+1])) + dp[i+2] 
        dp[i] = max(notMakePair, makePair) # minh chi chon cai kq ghep nao lon nhat thoi
        print(dp)
    return dp[0]


print(solution([2, 2, 3, 5, 4, 0])) # Output: 97
print(solution([3, 19, 191, 91, 3])) # Output: 20107
