from t
def solution(M, N):
    x = int(math.sqrt(4 * N + M))
    if x % 2 == 0:
        return x
    else:
        inter = ((x - 1) * (x - 1)) // 4
        if 4 * min(inter, N) + M >= x * x:
            return x
        else:
            return x - 1
 
print(solution(8, 0))


