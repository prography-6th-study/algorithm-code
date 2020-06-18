"""
dictionary에 value를 배열로 넣고 sorting 하여 
알파벳 순서가 앞서는 경로를 먼저 return시키는 것은 바로 구현했으나,
'주어진 항공권을 모두 사용해야 한다' 는 조건을 간과하여 bfs로 접근하였고 테스트케이스 1, 2 가 실패하였음.

dfs 구현은 타 블로그 코드 일부 참고하였음. 재귀와 stack 중 구현이 간단해보이는 stack을 택하였음.
tree의 말단(leaf node)부터 경로에 append되기 때문에 ret[::-1] 을 통해 뒤집어주는 과정이 필요하였다.
"""

from collections import deque


def solution_first(tickets):
    q = deque(["ICN"])
    ret, d = [], dict()
    for t in tickets:
        d[t[0]] = d.get(t[0], []) + [t[1]]
        d[t[0]].sort(reverse=True)
    while q:
        cur = q.popleft()
        ret.append(cur)
        if cur in d and d[cur]:
            next_a = d[cur][-1]
            d[cur].remove(next_a)
            q.append(next_a)
    return ret


def solution(tickets):
    d, ret = dict(), []
    s = ['ICN']
    for t in tickets:
        d[t[0]] = d.get(t[0], []) + [t[1]]
        d[t[0]].sort(reverse=True)
    while len(s) > 0:
        cur = s[-1]
        if cur in d and d[cur]:
            s.append(d[cur][-1])
            d[cur].pop()
        else:
            ret.append(s.pop())
    return ret[::-1]


t = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(t))
