import pytest


def solution(citations):
    citations.sort(reverse=True)
    # print(citations)
    answer = 0
    for idx, c in enumerate(citations):
        if idx < c:
            answer = idx + 1
        else:
            break
    return answer


@pytest.mark.parametrize("citations, expected", [
    ([3, 0, 6, 1, 5], 3),
    ([2,2,2,2,2], 2),
    ([5, 5, 5, 5], 4),
    ([0, 0, 0, 0], 0)
])
def test_simple(citations, expected):
    assert solution(citations) == expected

"""
[ 풀이 방법 ]
    - 문제가 이해가 안갔다. 검색해보니까 인덱스 값보다 배열 값이 큰 개수를 세면 된다고 했다.
    - 그래도 뭔 말인지 모르겠음 ㅜㅜ

"""