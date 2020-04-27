import pytest


def solution(answers):
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if man1[idx % len(man1)] == ans:
            count[0] += 1
        if man2[idx % len(man2)] == ans:
            count[1] += 1
        if man3[idx % len(man3)] == ans:
            count[2] += 1

    answer = [idx+1 for idx, x in enumerate(count) if x == max(count)]
    return answer


@pytest.mark.parametrize("answers, expected", [
    ([1, 2, 3, 4, 5], [1]),
    ([1, 3, 2, 4, 2], [1, 2, 3]),
])
def test_simple(answers, expected):
    assert solution(answers) == expected
