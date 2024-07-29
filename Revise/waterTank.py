# O(N ^ 2)
# s = '-HH-H-H-H-H---H-H--H'

# if "HHH" in s or s[:1] == 'HH' or s[-2:] == 'HH' or len(s) <= 1:
#     print("FINAL count:", count)
    
# else:

# count = 0
# for i in range(len(s) - 1):
#     if s[i] == 'H' and s[i + 1] == '-':
#         s = s.replace('H', 'd',1)
#         count += 1
#         if s[i + 2] == 'H':
#             s = s.replace('H', 'd',1)
#     elif s[i] == 'H' and s[i + 1] == 'H':
#         s = s.replace('H', 'd',1)
#         count += 1
#     #print(s)
        
# if s[-1] == 'H':
#     count += 1
#     s = s.replace('H', 'd', 1)
        
#print(count)
# ----------------------------------------------------------------
# O(N)
s = '-H-H-H-H-H'
def solution(s):
    count = -1
    if "HHH" in s or s[:1] == 'HH' or s[-2:] == 'HH' or len(s) <= 1:
        return count
        
    house = []
    done = [-1]
    for i in range(len(s)):
        if s[i] == 'H':
            house.append(i)
    # print("Origin house:", house)
        
    count = 0
    for i in range(len(house) - 1):
        idx = house[i]
        if done[-1] != idx and s[idx] == 'H' and s[idx + 1] == '-':
            done.append(idx)
            
            count += 1
            if done[-1] != idx + 2 and s[idx + 2] == 'H':
                done.append(idx + 2)
                
        elif done[-1] != idx + 1 and s[idx] == 'H' and s[idx + 1] == 'H':
            
            done.append(idx)
            count += 1
        # print("Done:", done)
            
    if done[-1] != len(s) - 1 and s[-1] == 'H':
        count += 1
        
    return count
    
# print(house)
print(solution(s))
