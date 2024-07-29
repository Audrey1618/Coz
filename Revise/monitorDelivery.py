# https://www.chegg.com/homework-help/questions-and-answers/code-javascript-given-set-orders-calculate-many-fulfilled-task-description-technology-comp-q129186925

def solution(D, C, P):
    count = 0
    distance = {}
    for i, d in enumerate(D):
        distance[D[i]] = C[i]

    distance = dict(sorted(distance.items()))
    print(distance)

    remain = P

    for value in distance.values():
        if remain < value:
            break
        count += 1
        remain = remain - value

    return count


print(solution([5, 5,5,5], [4,9,2,3], 10))