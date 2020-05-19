import pytest
from collections import deque


def solution(n, computers):
    dfs = []
    visit = [False] * n
    answer = 0
    for i in range(n):
        if visit[i] is True:
            continue
        answer += 1
        dfs.append(i)
        while dfs:
            now = dfs.pop()
            for idx, j in enumerate(computers[now]):
                if j == 1 and visit[idx] is False:
                    visit[idx] = True
                    dfs.append(idx)
    return answer


@pytest.mark.parametrize(
    "n, computers, expected",
    [
        (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1),
    ],
)
def test_simple(n, computers, expected):
    assert solution(n, computers) == expected


"""
[ 풀이 방법 ]
    연결된 노드를 찾는 거라서 dfs문제라고 생각햇다.

    index로 연결된 컴퓨터에 접근했다.
    연결 된 컴퓨터에서 또 연결된 것들을 bfs[]에 넣어주고, 방문 체크를 했다

    while bfs: 문이 끝나면 연결된 컴퓨터가 없다는 것으로 answer을 +1 해준다.
"""
