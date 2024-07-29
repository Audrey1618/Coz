# https://algo.monster/problems/string_without_3_identical_consecutive_letters


def solution(s):
    news = s[0:2]
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            news += s[i]
    return news


print('eedaaad || res =', solution('eedaad'))
# res = eedaad
print('xxxtxxx || res =', solution('xxxtxxx')) # res = xxtxx
print('uuuuxaaaaxum || res =', solution('uuuuxaaaaxum')) # uuxaaxum

