# https://leetcode.com/discuss/interview-question/1458197/difficult-hudson-river-trading-question-oa

def suitableLocations(K, A): # Manhattan distance O(N²) of number of locations
    loc = [], []
    for i, row in enumerate(A):
        for j, k in enumerate(row):
            loc[k].append((i, j))

    return sum(all(abs(x - i) + abs(y - j) <= K for x, y in loc[1]) for i, j in loc[0])