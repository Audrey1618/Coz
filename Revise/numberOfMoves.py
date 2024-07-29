# https://www.chegg.com/homework-help/questions-and-answers/given-array-consisting-n-integers-within-range-1n--one-move-increase-decrease-value-elemen-q121018756

def solution(A):
    A.sort()
    # [1, 1, 2]
    # [0, 1, 2]

    res = 0
    for i in range(len(A)):
        res += abs(A[i] - (i + 1))
    return res


print("[1, 2, 1] || res =", solution([1, 2, 1])) # res = 2
print("[2, 1, 4, 4] || res =", solution([2, 1, 4, 4])) # res = 1
print("[6, 2, 3, 5, 6, 3] || res =", solution([6, 2, 3, 5, 6, 3])) # res = 4

