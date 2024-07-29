A = [3,2,-2,5,-3, -5, 7, -7, 5, -5]
A = [1, 2, 3, -4]

A.sort()
print(A)
exist = []
res = 0
for i in range(len(A)):
    comple = -A[i]
    if comple in exist:
        res = max(res, abs(comple))
    else:
        exist.append(A[i])
print(res)
