# https://www.numerade.com/ask/question/texts-write-solution-in-javascript-language-a-string-made-of-an-even-number-of-characters-andor-is-called-symmetric-if-all-characters-in-its-first-half-are-and-all-characters-in-its-second-h-40342/
s = '<><??>>'
# <>< <<>>
# res = 4
# S = '??????' # res = 6
s = '<<?' # res = 2

def count_longest_sym_substr(s):
    result = 0
    i = 0
    while i < len(s):
         # if the result is already >= the rest of the string, no point processing further
        rest_len = len(s) - i
        if result >= rest_len:
            return result
        
        l = i
        r = i + 1
        
        while l >= 0 and r < len(s) and s[l] == "<" and s[r] == ">":
            sub_len = r - l + 1
            result = max(result, sub_len)
            l -= 1
            r += 1

        i = r

    return result

def solution(s: str) -> int:
    if "?" not in s:
        return count_longest_sym_substr(s)

    return max(
        solution(s.replace("?", "<", 1)),
        solution(s.replace("?", ">", 1)),
    )
    
print(solution(s))
