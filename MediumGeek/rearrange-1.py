a = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# a = [-1, -1, 1, 2, 3, -1, 4, -1, 6, -1, -1, 9]
s = set()
# Storing all the values in the Set
for i in range(len(a)):
    s.add(a[i])
print(s)

# res = [0,0,0,....,0]

for i in range(len(a)):
    # check for item if present in set
    if i in s:
        a[i] = i
    else:
        a[i] = -1

print(a)


