A = [4, 5, 10, 3, 2, 20, 100, 80]


# dk 5, 4 , 10

for i in range(1, len(A) - 1, 2):
    if A[i - 1] > A[i] and A[i] > A[i + 1]:
        A[i], A[i + 1] = A[i + 1], A[i]
    
    elif A[i - 1] < A[i] and A[i] < A[i + 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
    

print(A)