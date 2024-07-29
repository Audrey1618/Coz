# https://www.chegg.com/homework-help/questions-and-answers/write-function-solution-given-string-s-consisting-n-characters-returns-alphabetically-smal-q108551137

s = 'abcda'
# res = 'ab'

# 132 -> remove 3

def solution(s):
    for i in range(len(s) - 1):
        # print(ord(s[i]), s[i])
        # print(ord(s[i + 1]), s[i + 1])
        if ord(s[i]) > ord(s[i + 1]):
            return s[:i] + s[i + 1:]
    return s[:-1]

print(solution(s))