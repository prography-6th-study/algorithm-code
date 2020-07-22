import pytest


def solution(board, moves):
    temp = []
    answer = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if len(temp) > 0 and temp[-1] == b[m-1]:
                    answer += 2
                    temp.pop()
                else:
                    temp.append(b[m-1])
                b[m-1] = 0
                break
    return answer

@pytest.mark.parametrize("board, moves, expected", [
    ([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4], 4),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 1, 2, 3, 1, 2, 3], 6)
])
def test_simple(board, moves, expected):
    assert solution(board, moves) == expected

"""
[ 풀이 방법 ]
- 
"""