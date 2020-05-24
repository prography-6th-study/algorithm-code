import pytest
from collections import deque


def solution(n, edge):
    answer = [0] * (n + 1)
    visited = [True] + [False] * n

    # 연결된 노드 넣어주기
    linked = [[] for _ in range(n + 1)]
    for k, v in edge:
        linked[k].append(v)
        linked[v].append(k)
    print(linked)

    # bfs
    for key, value in enumerate(linked):
        queue = deque([])
        # 방문 확인
        if visited[key] is True:
            continue

        visited[key] = True
        for v in value:
            queue.append(v)
            visited[v] = True
            answer[v] += 1

        while queue:
            now = queue.popleft()
            for t in linked[now]:
                if visited[t] is True:
                    continue
                queue.append(t)
                visited[t] = True
                answer[t] += answer[now] + 1

    # 가장 큰 값 개수 세기
    max_num = max(answer)
    return answer.count(max_num)


@pytest.mark.parametrize(
    "n, edge, expected", [(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]], 3)],
)
def test_simple(n, edge, expected):
    assert solution(n, edge) == expected


"""
[ 풀이방법 ]
    - 그래프 문제는 bfs, dfs로 풀면 되는 것 같다.
    - 가장 먼 노드를 찾을 때는 bfs를 활용하면 된다.
"""
