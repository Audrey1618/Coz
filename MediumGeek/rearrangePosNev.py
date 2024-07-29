a = [-1, 2, -3, 4, 5, 6, -7, -8, -9]
# res = [9, -7, 8, -3, 5, -1, 2, 4, 6]
res = []
pos = []
nev = []
for i in range(len(a)):
    if a[i] >= 0:
        pos.append(a[i])
    else:
        nev.append(a[i])
print(pos, nev)


for i in range(min(len(pos), len(nev))):
    res.append(pos[i])
    res.append(nev[i])

p = len(pos)
n = len(nev)

for i in range(abs(p - n)):
    if p > n:
        res.append(pos[n + i])
    else:
        res.append(nev[p + i])


print(res)

