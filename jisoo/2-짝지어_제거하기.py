import pytest


def solution(s):
    s = list(s)
    temp = []

    for idx in range(len(s)):
        if len(temp) == 0:
            temp.append(s[idx])
        elif s[idx] != temp[-1]:
            temp.append(s[idx])
        elif s[idx] == temp[-1]:
            temp.pop()

    if len(temp) == 0:
        return 1
    else:
        return 0

@pytest.mark.parametrize("s, expected", [
    ("baabaa", 1),
    ("cdcd", 0)
])
def test_simple(s, expected):
    assert solution(s) == expected

"""
[ 풀이 방법 ]
- 처음에는 리스트 원소들을 삭제하면서 리스트를 변경했는데 시간초과가 났다.
그래서 temp리스트를 두고 비교를 해주었다.
"""