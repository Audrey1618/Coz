a = [1, 2, 3, 4, 5]
charSet = set()
res = []
for num in a:
    if num not in charSet:
        res.append(num)
    charSet.add(num)

print(res)