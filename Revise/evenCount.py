def solution(s):
    exist = {0:-1}
    chars = 'abcdefghijklmnopqrstuvwxyz'
    state = 0
    res = 0
    
    for i in range(len(s)):
        j = chars.find(s[i])
        # print(j)
        state ^= 1 << j
        if state not in exist:
            exist[state] = i
        res = max(res, i - exist[state])
        # print("s[i]:", s[i])
        # print(exist[state])
    return res
    
s = 'abcabckmabcabcdd' 

print(solution(s))