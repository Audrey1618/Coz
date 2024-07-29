# https://media.cheggcdn.com/media/a0c/a0cd2a2a-7c54-476f-a93c-93e8b36d1780/phpNsErQL.png
import math
A = [3, 5, 6, 3, 3, 5]
count = 0
# searched = set()
for i in range(len(A)):
    # if i in searched:
    #     continue
    r = i + 1
    while r < len(A):
        if A[r] == A[i]:
            count += 1
        r += 1

# print(count)
exist = {}
for i in range(len(A)):
    exist[A[i]] = exist.get(A[i], 0 ) + 1
print(exist)
res = 0
for key, val in exist.items():
    if val > 1:
        res += math.comb(val, 2) 

print(res)

print(math.comb(pow(10,5), 2))