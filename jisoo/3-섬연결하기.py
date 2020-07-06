import pytest


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    check = {costs[0][0], costs[0][1]}
    answer = costs[0][2]
    costs = costs[1:]

    while len(check) != n:
        for n1, n2, cost in costs:
            if n1 in check and n2 in check:
                continue
            if n1 in check or n2 in check:
                check.add(n2)
                check.add(n1)
                answer += cost
                costs.remove([n1, n2, cost])
                break
    return answer


@pytest.mark.parametrize("n, costs, expected", [
    (4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]], 4)
])
def test_simple(n, costs, expected):
    assert solution(n, costs) == expected

"""
[ 풀이 방법 ]
- cost[i][2] 작은 값으로 정렬하고 되는지 안되는지 선택...?

역시나 인터넷을 찾아봤다. 아직 3단계는 힘든건가ㅜㅅㅜ
크루스칼 알고리즘을 사용하면 된다고 한다.

[크루스칼 알고리즘]
그리디 방법을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 방법

동작 방법
- 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
- 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
    즉, 가장 낮은 가중치를 먼저 선택한다. 사이클을 형성하는 간선은 제외한다.
- 해당 간선을 현재의 최소 비용 신장 트리의 집합에 추가한다.

사이클이 생기는지 확인하는 방법
- 추가할 새로운 간선의 양 끝 정점이 같은 집합에 속해 있으면 사이클이 형성된다.

[문제 풀면서 생긴 궁금증]
- 왜 14번째 줄 if문을 걸어야 하는건지 모르겠다.
"""