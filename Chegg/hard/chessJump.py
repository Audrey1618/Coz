# https://www.chegg.com/homework-help/questions-and-answers/codility-challenge-idea-come-solution-know-asks-python-didn-t-want-start-timer-found-pictu-q99194003
A = [2, 3, -1, 1, 3]
A = [1, 1, -1, 1]

def solution(A):
    count = 0
    visit = set()
    l = 0
    while l < len(A):
        l = l + A[l]
        if l in visit:
            return -1
        
        visit.add(l)
        count += 1
    
    return count

print(solution(A))