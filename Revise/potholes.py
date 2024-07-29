Potholes easy:

S = '.x..x'
#res = 3
count = 0
exist = []
total = S.count('x')

r = 0

while r < len(S):
    if S[r] == 'x':
        count += 1
        r += 3
    else:
        r += 1

print(count)

# ------------------------------------
Potholes medium:

L1 = '..xx.x.'
L2 = 'x.x.x..'

count1 = L1.count('x')
count2 = L2.count('x')

L1_left = [0]
L1_right = [count1]

L2_left = [0]
L2_right = [count2]

for i in range(len(L1)):
    if L1[i] == 'x':
        L1_right.append(L1_right[-1] - 1)
        L1_left.append(count1 - L1_right[-1] - 1)
    elif L1[i] == '.':
        L1_right.append(L1_right[-1])
        L1_left.append(count1 - L1_right[-1])
    
for i in range(len(L2)):
    if L2[i] == 'x':
        L2_right.append(L2_right[-1] - 1)
        L2_left.append(count2 - L2_right[-1] - 1)
    elif L2[i] == '.':
        L2_right.append(L2_right[-1])
        L2_left.append(count2 - L2_right[-1])


print("L1_left: ", L1_left)
print("L2_right:", L2_right)

print("L1_right:", L1_right)
print("L2_left: ", L2_left)

res = 0
for i in range(len(L1)):
    res = max(res, L1_left[i] + L2_right[i], L1_right[i] + L2_left[i])
    
print(res)
