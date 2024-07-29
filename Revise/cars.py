# https://leetcode.com/discuss/interview-question/2058599/a-group-of-friends-is-going-on-holiday-together-codility-problem
remain = sum(P) 

S = sorted(S, reverse = True) # xếp theo chiều từ lớn đến bé

print(S)
count = 0
i = 0
while remain > 0:
    remain -= S[i]
    count += 1
    i += 1

print(i)