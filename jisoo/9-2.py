import pytest


def solution(n):
    num = 0
    i, j = -1, 0
    answer = [[0] * n for _ in range(n)]
    for order in range(n):
        for count in range(order, n):
            print(i, j, num, '-', order, count)
            if order % 3 == 0:
                # 왼쪽 면
                i += 1
            elif order % 3 == 1:
                # 아래 면
                j += 1
            elif order % 3 == 2:
                # 오른쪽 면
                i -= 1
                j -= 1
            num += 1
            answer[i][j] = num
    answer = [element for array in answer for element in array if element != 0]
    return answer


@pytest.mark.parametrize("n, expected", [
    (4, [1,2,9,3,10,8,4,5,6,7])
    # ,
    # (5, [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]),
    # (6, [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])
])
def test_simple(n, expected):
    assert solution(n) == expected

"""
[ 풀이 방법 ]

"""