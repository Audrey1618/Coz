s = 'BACABACACBCBABAC' #-> res = 'CB' -> shortest

def shortest(s):
    exist = {}
    l, r = 0, 0
    for r in range(len(s)):
        exist[s[r]] = exist.get(s[r], 0) + 1
    
    if 1 in exist.values():
        return 1
    
    else:
        for i in range(2, len(s)):
            check = []
            l, r = 0, 0
            while r < len(s):
                r = l + i - 1
                if s[l: r + 1] not in check:
                    if s.count(s[l: r + 1]) == 1:
                        print(s[l: r + 1])
                        return i
                    elif s.count(s[l: r + 1]) > 1:
                        check.append(s[l: r + 1])
                l += 1
               
        
print(shortest(s))