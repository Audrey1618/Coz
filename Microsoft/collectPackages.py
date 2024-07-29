# https://leetcode.com/discuss/interview-question/4652562/Microsoft-OA

def solution(A):
    stack = [0]
    res = 0
    j = 0
    for i in range(len(A)):
        while A[i] != stack[-1] and j < max(A):
            j += 1
            stack.append(j)
        
        if j == max(A) - 1:
            return res

        stack.pop()
        res = max(res, len(stack) - 1)
        # print(stack, res)
            
    return res

print("[3, 2, 4, 5, 1]", solution([3, 2, 4, 5, 1])) # res = 2

print("[1, 2, 3, 4, 5]", solution([1, 2, 3, 4, 5])) # res = 0

print("[3, 2, 7, 4, 5, 6, 1]", solution([3, 2, 7, 4, 5, 6, 1])) # res = 4

