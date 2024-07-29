# https://algo.monster/problems/min_steps_to_make_piles_equal_height

def solution(v):
    n = len(v) # n = 3
    if n < 2:
        return 0
    v.sort()
    # 1 2 5
    #   t s
    # s   t  
    res = 0
    for i in range(1, n):
        if v[n - i - 1] != v[n - i]:
            res += i
    return res

print('[5, 2, 1] || res =', solution([5, 2, 1])) # res = 3
