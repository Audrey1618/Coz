# https://leetcode.com/discuss/interview-question/555715/microsoft-online-codility-assessment-l-r-commands-task-3

# N = -11 #res = 4

def solution(N):

    def lcommand(l, r):
        l = 2 * l - r
        return (l, r)

    def rcommand(l, r):
        r = 2 * r - l
        return (l, r)
   
    def bfs(start, target):
        visited = set([start])
        q = [start]
        steps = 0
        while q:
            for _ in range(len(q)):
                l, r = q.pop(0)
                for cmd in [lcommand, rcommand]:
                    nl, nr = cmd(l, r)
                    if (nl, nr) in visited:
                        continue
                    if nl == target or nr == target:
                        return steps + 1
                    q.append((nl, nr))
            steps += 1
        return -1

    return bfs((0, 1), N)

print(solution(18))