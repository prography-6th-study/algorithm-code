import pytest

answer = [0, 0]


def compression(arr, x, y, check_length):
    sum = 0

    for i in range(x, x+check_length):
        for j in range(y, y+check_length):
            sum += arr[i][j]

    if sum == 0:
        answer[0] += 1
        return
    elif sum == check_length*check_length:
        answer[1] += 1
        return
    else:
        next_length = check_length // 2
        compression(arr, x, y, next_length)
        compression(arr, x, y + next_length, next_length)
        compression(arr, x + next_length, y, next_length)
        compression(arr, x + next_length, y + next_length, next_length)


def solution(arr):
    compression(arr, 0, 0, len(arr))
    return answer


@pytest.mark.parametrize("arr, expected", [
    ([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]], [4,9])
    # ([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]], [10, 15])
])
def test_simple(arr, expected):
    assert solution(arr) == expected

"""
[ 풀이 방법 ]
- 
"""