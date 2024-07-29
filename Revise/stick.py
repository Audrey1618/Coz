A = 13
B = 10
def stick(A, B):
    limit = (A + B) // 4
    # print(limit)
    for i in range(limit, 0, -1):
        # print(i)
        if (4 * i <= B) or (i <= A and 3 * i <= B) or (2 * i <= A and 2 * i <= B) or (4 * i <= A):
            return i
    return 0
            
print(stick(A, B))

# ------------------------------------------requiredSideLenForSquare=4
def countPieces(cutLen):
    sticksFormed = A // cutLen + B // cutLen
    if sticksFormed >= requiredSideLenForSquare:
        return True
    return False

def canFormSquare(A,B)
    l = 1
    r = (A+B)//4
    ans = 0
    while l <= r:
        mid = (l + r)//2
        if countPieces(mid):
            ans = l
            l = mid + 1
        else:
            r = mid - 1
    return ans