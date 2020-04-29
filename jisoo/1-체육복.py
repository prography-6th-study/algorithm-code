import pytest


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    print(set_lost, set_reserve)
    check = 0
    for l in set_lost:
        if l - 1 in set_reserve:
            set_reserve.remove(l - 1)
            check += 1
        elif l + 1 in set_reserve:
            set_reserve.remove(l + 1)
            check += 1
    answer = n - len(set_lost) + check
    return answer


@pytest.mark.parametrize(
    "n, lost, reserve, expected",
    [
        (5, [2, 4], [2, 3, 5], 5),
        (5, [2, 4], [1, 3, 5], 5),
        (3, [3], [1], 2),
        (30, [1, 9, 11, 14], [2, 10], 28),
        (5, [2, 4], [3], 4),
        (8, [3, 4, 7, 8], [1, 2, 3, 4, 5, 7, 8], 8),
        (7, [2, 3, 4], [1, 2, 3, 6], 6),
    ],
)
def test_simple(n, lost, reserve, expected):
    assert solution(n, lost, reserve) == expected


"""풀이방법
잃어 버린 학생에서 여분을 가지고 있는 학생을 일단 빼준다.
그 다음 잃어 버린 학생을 돌면서 빌릴 수 있으면 빌린다.
빌려주면 reserve에서 값을 제거해준다.
"""
