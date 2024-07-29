# https://algo.monster/problems/longest_semi_alternating_substring

def solution(s: str) -> int:
    res = 0
    l = 0
    for r in range(len(s)):
        if r - l + 1 >= 3 and s[r] == s[r - 1] == s[r - 2]:
            l = r - 1
        res = max(res, r - l + 1)
    return res


print('baaabbabbb || res =', solution('baaabbabbb')) # res = 7
print('babba || res =', solution('babba')) # res = 5
print('abaaaa || res =', solution('abaaaa')) # res = 4