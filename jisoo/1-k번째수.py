import pytest


def solution(array, commands):
    answer = []
    for c in commands:
        arr = array[c[0]-1:c[1]]
        arr.sort()
        print(arr)
        answer.append(arr[c[2]-1])
    return answer


@pytest.mark.parametrize("array, commands, expected", [
    ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5, 6, 3])
])
def test_simple(array, commands, expected):
    assert solution(array, commands) == expected


"""풀이 방법
slice 를 이용해서 풀어줬다.
slice [start:end] 라고 하면 end는 포함하지 않음!
"""
