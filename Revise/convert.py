def convert(s, t):
    if s == t:
        return 'EQUAL'
    
    if len(s) + 1 == len(t):
        insert = True
        for i in range(len(s)):
            # print(s[i], t[i + 1])
            if s[i] != t[i + 1]:
                insert = False
        if insert == True:
            return 'INSERT ' + t[0]
        else:
            return 'IMPOSSIBLE'
    
    elif len(s) - 1 == len(t):
        remove = True
        for i in range(len(t) - 1):
            # print(s[i], t[i])
            if s[i] != t[i]:
                remove = False
        if remove == True:
            return 'REMOVE ' + s[-1]
        else:
            return 'IMPOSSIBLE'
    
    elif len(t) == len(s):
        existS = [0] * 26
        existT = [0] * 26
        
        swap = False
        for i in range(len(t)):
            existS[ord(s[i]) - ord('a')] += 1
            existT[ord(t[i]) - ord('a')] += 1
       
        if existT != existS:
            return 'IMPOSSIBLE'
            
        if existT == existS:
            swap = True
    
            for i in range(len(t)):
                if s[i] != t[i]:
                    return 'SWAP ' + s[i] + ' ' + t[i]
    
    else:
        return 'IMPOSSIBLE'
        
print(convert(s, t))

# -------------------------------------------------def convert(s, t):
    if s == t:
        return 'EQUAL'
    
    if len(s) + 1 == len(t) and s == t[1:]:
        return 'INSERT ' + t[0]
     
    elif len(s) - 1 == len(t) and t == s[:len(s) - 1]:
        return 'REMOVE ' + s[-1]
    
    elif len(t) == len(s):
        existS = [0] * 26
        existT = [0] * 26
        
        swap = False
        for i in range(len(t)):
            existS[ord(s[i]) - ord('a')] += 1
            existT[ord(t[i]) - ord('a')] += 1
     
        if existT == existS:
            swap = True
    
            for i in range(len(t)):
                if s[i] != t[i]:
                    return 'SWAP ' + s[i] + ' ' + t[i]
    
    return 'IMPOSSIBLE'
        
print(convert(s, t))