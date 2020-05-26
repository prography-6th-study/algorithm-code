"""
deque를 이용해 구현하였다. 
구현은 별로 어렵지 않았으나, 문제에 대기목록의 앞/뒤가 헷갈리게 적혀있어서 조금 헤맸다.
"""

from collections import deque

def solution(priorities, location):
    q = deque()
    for idx, i in enumerate(priorities):
        q.append((i, idx))
    cnt = 0
    while True:
        if len(q) == 1:
            cnt += 1
            break
        J = q.popleft()
        if J[0] < max(q)[0]:
            q.append(J)
        else:
            cnt += 1
            if J[1] == location:
                break
    return cnt


p = [2, 1, 3, 2]
l = 2

p2 = [1, 1, 9, 1, 1, 1]
l2 = 0

p3 = [3, 3, 4, 2]
l3 = 3

solution(p3,l3)