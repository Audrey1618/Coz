a = [12, 11, -13, -5, 6, -7, 5, -3, -6]
# res = [-13 -5 -7 -3 -6 12 11 6 5]

p, n = len(a) // 2, 0
for i in range(len(a)):
    if a[i] < 0:
        a[i], a[n] = a[n], a[i]
        n += 1

    
print(n)
count = 0
for i in range(len(a)):
    if a[i] > 0:
        res[n + count] = a[i]
        count += 1
    print(res)