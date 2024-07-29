arr = [1, 3, 2]

for i in range(1, len(arr)):
    if i % 2 == 0:
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    else:
        if arr[i] > arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

print(arr)

        