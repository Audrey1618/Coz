# https://algo.monster/problems/max_length_of_a_concatenated_string_with_unique_characters
from typing import List
def solution(arr: List[str]) -> int:
    maxlen = 0
    unique = ['']

    def isvalid(s):
        return len(s) == len(set(s))

    for word in arr:
        print(word)
        for j in unique:
            print("j:", j)
            tmp = word + j
            if isvalid(tmp):
                unique.append(tmp)
                maxlen = max(maxlen, len(tmp))

    return maxlen
    
print(solution(["un","iq","ue"]))
