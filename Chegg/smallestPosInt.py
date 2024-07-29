A = [1, 3, 6, 4, 1, 2]
A = [-1, -3]
A = [-4, 2, 1, 3,4,5]
A = [-4, 0, 4, 3,3]

res = 1
A.sort()

for i in range(len(A)):
    if A[i] == res:
        res += 1
print(res)