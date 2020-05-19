import pytest

def solution(n, lost, reserve):
    cnt = 0
    same = set(lost) & set(reserve)
    reserve = list(set(reserve) - same)
    for i in list(set(lost) - same):
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            cnt += 1
    return n - cnt

@pytest.mark.parametrize("n, lost, reserve, expected", [
    (5, [2,4], [1,3,5], 5),
    (5, [2,4], [3], 4),
    (3, [3], [1], 2),
    (5, [1,2], [2,3], 4),
    (3, [1,2,3], [1,2,3], 3),
    (7, [2,3,4], [1,2,3,6], 6)
])
def test_simple(n, lost, reserve, expected):
    assert solution(n, lost, reserve) == expected