A = [1, 2, 3, 4, 5, 6]
res = []
l, r = 0, len(A) - 1

while l <= r:
    if l == r:
        res.append(A[r])
    else:
        res.append(A[r])
        res.append(A[l])
    r -= 1
    l += 1

print(res)
