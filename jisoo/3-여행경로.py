import pytest
from collections import Counter


def solution(tickets):
    dfs = ["ICN"]
    answer = []

    routes = {}
    for t in tickets:
        # 출발 공항이 키, value는 갈 수 있는 공항 들어있는 리스트
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    while dfs:
        now = dfs[-1]
        if now not in routes or len(routes[now]) == 0:
            answer.append(dfs.pop())
        else:
            dfs.append(routes[now].pop())
    answer.reverse()
    return answer

@pytest.mark.parametrize("tickets, expected", [
    ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]),
    ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]),
    ([['ICN','BOO'], [ 'ICN', 'COO'], [ 'COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']], ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO'])
])
def test_simple(tickets, expected):
    assert solution(tickets) == expected

"""
[ 풀이 방법 ]
- 항공권을 모두 이용해야 한다고해서 dfs라고 생각했다
- 그냥 넣어버리면 알파벳 순서대로 나오지가 않는다 그러고 경로가 끊기는 문제가 생긴다...

- 더이상 방문할 경우가 없는데 now가 된 경우를 어떻게 처리해야하나

- 그러다가 인터넷을 찾아봤는데 갈 곳이 없을 경우 answer 리스트에 담아주고 dfs에서 pop해주는게 인상적이었다.
- 그렇게 되면 자연스럽게 다 이어지니깐...
"""