from collections import deque 
a = [1, 3, 5, 7, 9]
a = deque(a)
k = 14

for i in range(k):
    a.append(a.popleft())

print(a)
    