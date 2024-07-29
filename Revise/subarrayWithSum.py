a = [1, 4, 0, 0, 3, 10, 5]
target = 7

l = 0
currSum = 0
for r in range(0, len(a)):
    currSum += a[r]

    while currSum > target:
        currSum -= a[l]
        l += 1

    if currSum == target:
        print(l, r)
        break

print('khong co subarray')