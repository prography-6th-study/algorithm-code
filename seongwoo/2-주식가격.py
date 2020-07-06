"""
큐에 있는 각 가격을 이중으로 순회하면서 값이 떨어지지 않을 때까지만 계속 값을 증가하는 식으로 구현.
"""

from collections import deque


def solution(prices):
    ret = []
    q = deque(prices)
    while q:
        cnt = 0
        end = q.popleft()
        for n in q:
            cnt += 1
            if end > n:
                break
        ret.append(cnt)
    return ret


p = [1, 2, 3, 2, 3]
print(solution(p))
