a = [1, 2, 3, 4, 5, 2]

res = [a[-1]]
# xet a tu day
# arr[] = {16, 17, 4, 3, 5, (2)} , curMax = 2 , ans[] = { 2 }
# arr[] = {16, 17, 4, 3, (5), 2} , curMax = 5 , ans[] = { 2, 5 }
# arr[] = {16, 17, 4, (3), 5, 2} , curMax = 5 , ans[] = { 2, 5 } 
# arr[] = {16, 17, (4), 3, 5, 2} , curMax = 5 , ans[] = { 2, 5 }
# arr[] = {16, (17), 4, 3, 5, 2} , curMax = 17 , ans[] = { 2, 5, 17 }
# arr[] = {(16), 17, 4, 3, 5, 2} , curMax = 17 , ans[] = { 2, 5, 17 }

for i in range(len(a) - 2, -1, -1):
    if a[i] > res[-1]:
        res.append(a[i])

print(res)