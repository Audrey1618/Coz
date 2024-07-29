# https://www.chegg.com/homework-help/questions-and-answers/m-trying-solve-c-t-seem-answer-correctly-q41325201
A = [1, 1, 0, 1, 1]

def solution(A):
    count = 0
    if len(A) == 1:
        return 0

    elif len(A) == 2:
        if A[0] == A[1]:
            return 1

    for i in range(1, len(A) - 1):
        if A[i - 1] != A[i] and A[i + 1] == A[i]:
            A[i + 1] = 1 - A[i]
            count += 1
        elif A[i - 1] == A[i] and A[i + 1] != A[i]:
            A[i - 1] = 1 - A[i]
            count += 1
        elif A[i - 1] == A[i] == A[i + 1]:
            A[i] == 1 - A[i - 1]
            count += 1
        print(A)
    return count

print(solution(A))

    