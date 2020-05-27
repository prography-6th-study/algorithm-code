import pytest


def solution(progresses, speeds):
    done = []
    for i, p in enumerate(progresses):
        day = 100-p
        done.append(day // speeds[i])
    print(done)

    max = done[0]
    count = 0
    answer = []
    for d in done:
        if max < d:
            answer.append(count)
            count = 1
            max = d
        else:
            count += 1
    answer.append(count)
    return answer



@pytest.mark.parametrize("progresses, speeds, expected", [
    ([93, 30, 55], [1, 30, 5], [2, 1])
])
def test_simple(progresses, speeds, expected):
    assert solution(progresses, speeds) == expected