# https://algo.monster/problems/max_inserts_to_obtain_string_without_3_consecutive_a

def max_inserts(s: str) -> int:
    ans, last = 0, '#'
    for c, g in groupby(s):
        L = len(list(g))
        if c == 'a':
            if L < 3:
                ans += 2 - L
            else:
                return -1
        else:
            ans += 2 * (L - (last == 'a'))
        last = c
    ans += 2 * (s[-1] != 'a')
    return ans